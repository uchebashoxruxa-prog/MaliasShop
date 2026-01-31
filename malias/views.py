from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView, UpdateView
from .forms import LoginForm, RegisterForm, DeliveryForm, EditUserForm, EditCustomerForm, ContactForm, CommentForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import CartForAuthUser, info_about_cart
import stripe
from shop.settings import STRIPE_SECRET_KEY


class MainPage(ListView):
    model = Product
    template_name = 'malias/main.html'
    context_object_name = 'products'
    extra_context = {'title': 'Malias - Electronics Store'}
    paginate_by = 12

    def get_queryset(self):
        products = Product.objects.all().order_by('-created_at')
        return products
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainPage, self).get_context_data()
        order_products = ProductOrder.objects.filter(quantity__gt=1).order_by('-quantity')
        products = []

        for p in order_products:
            if p.product in products:
                continue
            products.append(p.product)

        context['order_products'] = products
        return context


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        product = context['product']
        context['title'] = product.title
        context['same_products'] = Product.objects.filter(category=product.category).exclude(
            pk=product.pk).order_by('-created_at')[:12]
        context['comments'] = Comment.objects.filter(product=product)
        context['comment_form'] = CommentForm()

        return context


def auth_user_page(request):
    if not request.user.is_authenticated:
        context = {
            'title': 'Authorization/Registration',
            'log_form': LoginForm(),
            'reg_form': RegisterForm()
        }

        return render(request, 'malias/auth.html', context)
    else:
        return redirect('main')


def login_user_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                if user:
                    login(request, user)
                    return redirect('main')

            messages.error(request, 'Invalid login or password')
            return redirect('auth')

    else:
        return redirect('main')


def logout_user_view(request):
    logout(request)
    return redirect('main')


def register_user_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                customer = Customer.objects.create(user=user)
                customer.save()
                cart = Cart.objects.create(customer=customer)
                cart.save()
                login(request, user)

            for err in form.errors:
                messages.error(request, form.errors[err].as_text())
            return redirect('auth')
    else:
        return redirect('main')


class ProductByCategory(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'malias/category.html'
    paginate_by = 12

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        qs = Product.objects.filter(category=category)

        model = self.request.GET.get('model')
        if model:
            qs = qs.filter(model__slug=model)

        color = self.request.GET.get('color')
        if color:
            qs = qs.filter(color_name=color)

        price_from = self.request.GET.get('price_from')
        if price_from:
            qs = qs.filter(price__gte=price_from)

        price_to = self.request.GET.get('price_to')
        if price_to:
            qs = qs.filter(price__lte=price_to)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['slug'])

        context['title'] = category.title
        context['models'] = category.models.all()
        context['prices'] = [i-100 if i != 100 else i for i in range(100, 11001, 1000)]
        context['colors'] = (Product.objects.filter(category=category).values_list('color_name', flat=True).distinct())

        return context


class SalesProducts(ListView):
    template_name = 'malias/product_list.html'
    context_object_name = 'products'
    extra_context = {'title': 'Bestseller Products'}
    paginate_by = 12

    def get_queryset(self):
        order_products = ProductOrder.objects.filter(quantity__gt=1).order_by('-quantity')
        products = []

        for p in order_products:
            if p.product in products:
                continue
            products.append(p.product)

        return products


@login_required(login_url='auth')
def save_delete_favourite(request, slug):
    user = request.user
    product = Product.objects.get(slug=slug)
    favourites = FavouriteProduct.objects.filter(user=user)

    if product not in [i.product for i in favourites]:
        FavouriteProduct.objects.create(user=user, product=product)
    else:
        favourite = FavouriteProduct.objects.get(user=user, product=product)
        favourite.delete()

    next_page = request.META.get('HTTP_REFERER', 'main')

    return redirect(next_page)


class FavouriteListView(LoginRequiredMixin, ListView):
    model = FavouriteProduct
    template_name = 'malias/product_list.html'
    context_object_name = 'products'
    extra_context = {'title': 'Favorite Products'}
    login_url = 'auth'
    paginate_by = 12

    def get_queryset(self):
        favourites = FavouriteProduct.objects.filter(user=self.request.user).order_by('-created_at')
        products = [i.product for i in favourites]
        return products


@login_required(login_url='auth')
def action_with_cart(request, slug, action):
    cart = CartForAuthUser(request, slug, action)
    next_page = request.META.get('HTTP_REFERER', 'main')

    return redirect(next_page)


@login_required(login_url='auth')
def customer_cart_view(request):
    cart = info_about_cart(request)
    context = {
        'title': 'My Cart',
        'products_cart': cart['products_cart'],
        'cart': cart['cart']
    }

    return render(request, 'malias/my_cart.html', context)


@login_required(login_url='auth')
def checkout_view(request):
    cart = info_about_cart(request)
    if cart['products_cart']:
        context = {
            'title': 'Order processing',
            'products_cart': cart['products_cart'],
            'cart': cart['cart'],
            'form': DeliveryForm(),
            'user_form': EditUserForm()
        }

        return render(request, 'malias/checkout.html', context)
    else:
        return redirect('main')


def about_malias(request):
    context = {
        'title': 'About Us'
    }

    return render(request, 'malias/about_malias.html', context)


@login_required(login_url='auth')
def create_checkout_session(request):
    stripe.api_key = STRIPE_SECRET_KEY
    if request.method == 'POST':
        cart = info_about_cart(request)
        total_price = cart['cart'].cart_total_price

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': ', '.join(i.product.title for i in cart['products_cart'])},
                    'unit_amount': int(total_price) * 100
                },
                'quantity': 1
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('checkout'))
        )

        request.session[f'form_{request.user.pk}'] = request.POST

        return redirect(session.url)


class ProductByModel(ListView):
    model = Product
    context_object_name = 'model_products'
    template_name = 'malias/models.html'
    paginate_by = 12

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        model_obj = ModelProduct.objects.get(slug=self.kwargs['model_slug'], category=category)
        products = Product.objects.filter(category=category, model=model_obj)

        model = self.request.GET.get('model')
        if model:
            qs = products.filter(model__slug=model)

        color = self.request.GET.get('color')
        if color:
            products = products.filter(color_name=color)

        price_from = self.request.GET.get('price_from')
        if price_from:
            products = products.filter(price__gte=price_from)

        price_to = self.request.GET.get('price_to')
        if price_to:
            products = products.filter(price__lte=price_to)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category_slug'])
        context['model'] = ModelProduct.objects.get(slug=self.kwargs['model_slug'], category=context['category'])
        context['title'] = context['model'].title
        context['prices'] = [i-100 if i != 100 else i for i in range(100, 11001, 1000)]
        context['colors'] = (Product.objects.filter(category=context['category'], model=context['model'])
                             .values_list('color_name', flat=True).distinct())

        return context


def model_products(request, model_slug):
    products = Product.objects.filter(model__slug=model_slug)
    title = products.first().model if products.exists() else ''

    context = {
        'title': title,
        'model_products': products
    }

    return render(request, 'malias/models.html', context)


@login_required(login_url='auth')
def success_payment(request):
    cart = info_about_cart(request)
    try:
        form = request.session.get(f'form_{request.user.pk}')
        request.session.pop(f'form_{request.user.pk}')
    except:
        form = False

    if cart['products_cart'] and form:
        delivery_form = DeliveryForm(data=form)
        if delivery_form.is_valid():
            delivery = delivery_form.save(commit=False)
            delivery.customer = Customer.objects.get(user=request.user)
            delivery.save()

            cart_user = CartForAuthUser(request)
            cart_user.save_order(delivery)
            cart_user.clear_cart()
        else:
            return redirect('checkout')

        context = {'title': 'Successful Payment'}
        return render(request, 'malias/success.html', context)

    else:
        return redirect('main')


@login_required(login_url='auth')
def profile_customer(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        customer_form = EditCustomerForm(request.POST, instance=request.user.customer)

        if user_form.is_valid():
            user_form.save()

            if customer_form.is_valid():
                customer_form.save()

            data = user_form.cleaned_data
            user = User.objects.get(id=request.user.id)

            if user.check_password(data['old_password']):
                if data['new_password'] != data['old_password'] and data['new_password'] == data['confirm_password']:
                    user.set_password(data['new_password'])
                    user.save()
                    update_session_auth_hash(request, user)

            return redirect('profile')
    else:
        user_form = EditUserForm(instance=request.user)
        customer_form = EditCustomerForm(instance=request.user.customer)

    context = {
        'title': 'My Account',
        'user_form': user_form,
        'customer_form': customer_form,
        'order': Order.objects.filter(customer=request.user.customer).last()
    }

    return render(request, 'malias/profile.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'title': 'Contact with malias',
        'form': form
    }

    return render(request, 'malias/contact.html', context)


class CustomerOrders(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    extra_context = {'title': 'Order History'}
    login_url = 'auth'

    def get_queryset(self):
        orders = Order.objects.filter(customer=self.request.user.customer)
        return orders.order_by('-created_at')


class SearchProduct(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'malias/base.html'
    ordering = '-created_at'
    paginate_by = 12

    def get_queryset(self):
        word = self.request.GET.get('key', '')
        products = Product.objects.filter(title__icontains=word)
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        word = self.request.GET.get('key', '')
        context['title'] = f"{word}"
        return context

# def filter_model(request, slug):
#     category = Category.objects.get(slug=slug)
#     products = Product.objects.filter(category=category)
#     title = products.first().model if products.exists() else ''
#
#     context = {
#         'title': title,
#         'model_products': products
#     }
#
#     return render(request, 'malias/models.html', context)


def save_comment_product(request, slug):
    if request.user.is_authenticated and request.method == 'POST':
        try:
            product = Product.objects.get(slug=slug)
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.product = product
                comment.save()

            return redirect('product', product.slug)
        except:
            return redirect('main')

    else:
        return redirect('auth')


class CommentUpdate(UpdateView):
    form_class = CommentForm
    model = Comment

    def get_success_url(self):
        comment = Comment.objects.get(pk=self.kwargs['pk'])
        return reverse('product', kwargs={'slug': comment.product.slug})

    def form_valid(self, form):
        try:
            comment = Comment.objects.get(pk=self.kwargs['pk'], author=self.request.user)
            if self.request.user.is_authenticated:
                return super(CommentUpdate, self).form_valid(form)
            else:
                return redirect('main')
        except:
            return redirect('main')


def comment_delete(request, pk):
    if request.user.is_authenticated and request.method == 'POST':
        try:
            comment = Comment.objects.get(pk=pk)
            if comment.author == request.user:
                comment.delete()

            return redirect('product', comment.product.slug)
        except:
            return redirect('main')
    else:
        return redirect('main')

