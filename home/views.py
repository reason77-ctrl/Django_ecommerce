from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages


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

def review_item(request):
    if request.method == "POST":
        rating = request.POST['rating']
        review = request.POST['review']
        slog = request.POST['slog']
        username = request.user.username
        email = request.user.email
        user_review = Review.objects.create(
            rating = rating,
            review = review,
            username = username,
            email = email,
            slog = slog
        )
        user_review.save()
        return redirect(f'/products/{slog}')


class CategoryView(BaseView):
    def get(self, request, slog):
        cat_id = Category.objects.get(slog = slog).id
        self.views['cat_detail'] = Item.objects.filter(category= cat_id)

        return render(request, 'product-list.html', self.views)


class Product_detailView(BaseView):
    def get(self, request, slog):
        self.views['item_detail'] = Item.objects.filter(slog = slog)
        self.views['brand'] = Brand.objects.filter(status= 'active')
        self.views['reviews'] = Review.objects.filter(slog=slog,status= 'active')
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


class SearchView(BaseView):
    def get(self, request):
        # query = request.GET.get('search', None)
        if request.method == 'GET':
            query = request.GET['search']
            self.views['search_product'] = Item.objects.filter(discription__icontains = query)
            return render(request, 'search.html', self.views)
        return render(request, 'search.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        views = dict()
        views["message"] = "The Form is Submitted."
        return render(request, 'contact.html',views)
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        fname = request.POST['fname']
        lname = request.POST['lname']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'This username is already taken')
                return redirect('home:signup')

            elif User.objects.filter(email = email).exists():
                messages.error(request, 'This email is already taken')
                return redirect('home:account')

            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password,
                    first_name = fname,
                    last_name = lname
                )
                user.save()
                messages.success(request, 'You are registered.')
                return redirect('home:account')

        else:
            messages.error(request, 'The password did not match.')
            return redirect('home:account')
    return render(request, 'signup.html')


def cart(request,slog):
    user = request.user.username
    if Cart.objects.filter(slog = slog).exists():
        quantity = Cart.objects.get(username = user, slog = slog, checkout = False).quantity
        qty = quantity + 1
        Cart.objects.filter(username=user, slog=slog, checkout=False).update(quantity= qty)
        return redirect('home:my_cart')
    else:
        data = Cart.objects.create(
            username = user,
            slog = slog,
            quantity = 1,
            items = Item.objects.filter(slog= slog)[0]
        )
        data.save()
        return redirect('home:my_cart')


class CartView(BaseView):
    def get(self, request):
        user = request.user.username
        self.views['cart_product']= Cart.objects.filter(username= user, checkout= False)
        return render(request, 'cart.html', self.views)
#
#
# class AccountView(BaseView):
#     def get(self, request):
#         return render(request, 'my-account.html')


# class Product_detailView(BaseView):
#     def get(self, request):
#         return render(request, 'product-detail.html')
