from django import template
from malias.models import Category, FavouriteProduct, Product, ProductCart
from malias.utils import info_about_cart

register = template.Library()


@register.simple_tag()
def get_categories():
    cats = Category.objects.all()
    return cats


@register.simple_tag()
def get_favourites(user):
    favourites = FavouriteProduct.objects.filter(user=user)
    products = [i.product for i in favourites]
    return products


@register.simple_tag()
def get_hot_products():
    products = Product.objects.filter(discount__gt=0).order_by('-created_at')[:5]
    return products


@register.simple_tag(takes_context=True)
def get_products_cart(context):
    request = context['request']
    cart = info_about_cart(request)
    return cart


@register.simple_tag()
def get_cart_products(user):
    cart_products = ProductCart.objects.filter(cart__customer__user=user)
    products = [i.product for i in cart_products]
    return products


@register.simple_tag(takes_context=True)
def query_params(context, **kwargs):
    query = context['request'].GET.copy()

    for key, value in kwargs.items():
        if value is None:
            query.pop(key, None)
        else:
            query[key] = value

    return query.urlencode()
