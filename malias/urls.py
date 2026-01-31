from django.urls import path
from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product'),
    path('authentication/', auth_user_page, name='auth'),
    path('login/', login_user_view, name='login'),
    path('logout/', logout_user_view, name='logout'),
    path('register/', register_user_view, name='register'),
    path('category/<slug:slug>/', ProductByCategory.as_view(), name='category'),
    path('sales/', SalesProducts.as_view(), name='sales'),
    path('action_favourite/<slug:slug>/', save_delete_favourite, name='action_favourite'),
    path('favourites/', FavouriteListView.as_view(), name='favourites'),
    path('action_cart/<slug:slug>/<str:action>/', action_with_cart, name='action_cart'),
    path('basket/', customer_cart_view, name='basket'),
    path('checkout/', checkout_view, name='checkout'),
    path('about/', about_malias, name='about'),
    path('contact/', contact_view, name='contact'),
    path('payment/', create_checkout_session, name='payment'),
    path('profile/', profile_customer, name='profile'),
    path('success/', success_payment, name='success'),
    path('orders/', CustomerOrders.as_view(), name='orders'),
    path('search/', SearchProduct.as_view(), name='search'),
    path('save_comment/<slug:slug>/', save_comment_product, name='save_comment'),
    path('comment_update/<int:pk>/', CommentUpdate.as_view(), name='comment_update'),
    path('comment_delete/<int:pk>/', comment_delete, name='comment_delete'),
    path('gadgets/<slug:category_slug>/<slug:model_slug>/', ProductByModel.as_view(), name='model_products'),
    path('gadgets/<slug:model_slug>/', model_products, name='model'),

]


