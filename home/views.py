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
        self.views['items'] = Item.objects.filter(status='active')
        self.views['brands'] = Brand.objects.filter(status= 'active')
        self.views['ads'] = Ad.objects.all()
        # self.views['ads2'] = Ad.objects.filter(rank= 2)
        self.views['feedbacks'] = Feedback.objects.filter(status= 'active')

        return render(request, 'index.html', self.views)


class CategoryView(BaseView):
    def get(self, request, slog):
        cat_id = Category.objects.get(slog = slog).id
        self.views['cat_detail'] = Item.objects.filter(category= cat_id)

        return render(request, 'product-list.html', self.views)


class Product_detailView(BaseView):
    def get(self, request, slog):
        self.views['item_detail'] = Item.objects.filter(slog = slog)
        self.views['brand'] = Brand.objects.filter(status= 'active')
        self.views['count'] = []
        for i in self.views['brand']:
            count_food = Item.objects.filter(brand = i.id).count()
            d = {'name':i.name, 'count':count_food}
            self.views['count'].append(d)

        self.views['cat_count'] = Category.objects.filter(status= 'active')
        self.views['count_cat'] = []
        for i in self.views['cat_count']:
            count_food = Item.objects.filter(category = i.id).count()
            dd = {'name':i.name, 'image':i.image,'count_cat':count_food}
            self.views['count_cat'].append(dd)

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
