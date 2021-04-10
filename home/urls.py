from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('category/<slog>', CategoryView.as_view(), name= 'category'),
    path('products/<slog>', Product_detailView.as_view(), name= 'products'),
    path('search', SearchView.as_view(), name= 'search'),
    path('contact', contact, name= 'contact'),
    path('account', signup, name = 'account'),
    path('review', review_item, name= 'review'),
    path('cart/<slog>', cart, name='cart'),
    path('my_cart', CartView.as_view(), name= 'my_cart'),
]