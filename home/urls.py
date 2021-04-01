from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('product-list', ProductsView.as_view(), name= 'product-list'),
    path('product-detail', Product_detailView.as_view(), name= 'product-detail'),
    path('products/<slog>', Product_detailView.as_view(), name= 'products'),
    path('cart', CartView.as_view(), name= 'cart'),
    path('checkout', CheckoutView.as_view(), name= 'checkout'),
    path('my-account', AccountView.as_view(), name= 'my-account'),
]