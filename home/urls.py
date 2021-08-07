from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('category/<slug>', CategoryView.as_view(), name= 'category'),
    path('products/<slug>', Product_detailView.as_view(), name= 'products'),
    path('search', SearchView.as_view(), name= 'search'),
    path('contact', contact, name= 'contact'),
    path('account', signup, name = 'account'),
    path('review', review_item, name= 'review'),
    path('cart/<slug>', cart, name='cart'),
    path('my_cart', CartView.as_view(), name= 'my_cart'),
    path('delete_cart/<slug>', delete_cart, name= 'delete_cart'),
    path('delete_single_cart/<slug>', delete_single_cart, name= 'delete_single_cart'),
    path('checkout', checkout, name='checkout'),
    path('checkouts', CheckoutView.as_view(), name= 'checkouts'),
    
]