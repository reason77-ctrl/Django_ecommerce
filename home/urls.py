from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('product-list', ProductsView.as_view(), name= 'product-list'),
    path('product-detail', Product_detailView.as_view(), name= 'product-detail'),
]