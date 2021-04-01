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
        self.views['brands'] = Brand.objects.filter(status= 'active')
        self.views['ads'] = Ad.objects.all()
        # self.views['ads2'] = Ad.objects.filter(rank= 2)
        # self.views['ads3'] = Ad.objects.filter(rank= 3)
        # self.views['ads4'] = Ad.objects.filter(rank= 4)
        # self.views['ads5'] = Ad.objects.filter(rank= 5)
        # self.views['ads6'] = Ad.objects.filter(rank= 6)
        # self.views['ads7'] = Ad.objects.filter(rank= 7)
        # self.views['ads8'] = Ad.objects.filter(rank= 8)
        self.views['feedbacks'] = Feedback.objects.filter(status= 'active')

        return render(request, 'index.html', self.views)


class ProductsView(BaseView):
    def get(self, request):
        self.views['items'] = Item.objects.filter(status='active')
        self.views['brands'] = Brand.objects.filter(status='active')
        return render(request, 'product-list.html', self.views)


class Product_detailView(BaseView):
    def get(self, request, slog):
        self.views['item_detail'] = Item.objects.filter(slog = slog)

        cat = Item.objects.get(slog = slog).category_id
        self.views['cat_items'] = Item.objects.filter(category = cat)
        return render(request, 'product-detail.html', self.views)


class CartView(BaseView):
    def get(self, request):
        return render(request, 'cart.html')


class CheckoutView(BaseView):
    def get(self, request):
        return render(request, 'checkout.html')


class AccountView(BaseView):
    def get(self, request):
        return render(request, 'my-account.html')


# class Product_detailView(BaseView):
#     def get(self, request):
#         return render(request, 'product-detail.html')
