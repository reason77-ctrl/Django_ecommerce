from django.shortcuts import render
from django.views.generic.base import View
from .models import *


# Create your views here.


class BaseView(View):
    views = {}


class HomeView(BaseView):
    def get(self, request):
        self.views['categories'] = Category.objects.filter(status='active')
        self.views['sliders'] = Slider.objects.filter(status='active')
        self.views['hotitems'] = Item.objects.filter(label='hot')
        self.views['newitems'] = Item.objects.filter(label='new')
        self.views['sales'] = Item.objects.filter(label='sale')
        self.views['defaults'] = Item.objects.filter(label='')

        self.views['ads'] = Ad.objects.all()
        # self.views['ads2'] = Ad.objects.filter(rank= 2)
        # self.views['ads3'] = Ad.objects.filter(rank= 3)
        # self.views['ads4'] = Ad.objects.filter(rank= 4)
        # self.views['ads5'] = Ad.objects.filter(rank= 5)
        # self.views['ads6'] = Ad.objects.filter(rank= 6)
        # self.views['ads7'] = Ad.objects.filter(rank= 7)
        # self.views['ads8'] = Ad.objects.filter(rank= 8)

        return render(request, 'index.html', self.views)


class ProductsView(BaseView):
    def get(self, request):
        return render(request, 'product-list.html')


class Product_detailView(BaseView):
    def get(self, request):
        return render(request, 'product-detail.html')


class CartView(BaseView):
    def get(self, request):
        return render(request, 'cart.html')


class CheckoutView(BaseView):
    def get(self, request):
        return render(request, 'checkout.html')


class Product_detailView(BaseView):
    def get(self, request):
        return render(request, 'product-detail.html')


class Product_detailView(BaseView):
    def get(self, request):
        return render(request, 'product-detail.html')
