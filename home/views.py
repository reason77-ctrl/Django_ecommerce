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
        slug = request.POST['slug']
        username = request.user.username
        email = request.user.email
        user_review = Review.objects.create(
            rating = rating,
            review = review,
            username = username,
            email = email,
            slug = slug
        )
        user_review.save()
        return redirect(f'/products/{slug}')


class CategoryView(BaseView):
    def get(self, request, slug):
        cat_id = Category.objects.get(slug = slug).id
        self.views['cat_detail'] = Item.objects.filter(category= cat_id)

        return render(request, 'product-list.html', self.views)


class Product_detailView(BaseView):
    def get(self, request, slug):
        self.views['item_detail'] = Item.objects.filter(slug = slug)
        self.views['brand'] = Brand.objects.filter(status= 'active')
        self.views['reviews'] = Review.objects.filter(slug=slug,status= 'active')
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

        cat = Item.objects.get(slug = slug).category_id
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


def cart(request,slug):
    user = request.user.username
    price = Item.objects.get(slug=slug).price
    discounted_price = Item.objects.get(slug=slug).discounted_price
    if Cart.objects.filter(slug = slug).exists():
        quantity = Cart.objects.get(username = user, slug = slug, checkout = False).quantity
        qty = quantity + 1
        
        if discounted_price > 0:
            actual_total = discounted_price * qty
           
        else:
            actual_total = price * qty
        
        Cart.objects.filter(username=user, slug=slug, checkout=False).update(quantity= qty,total=actual_total)
        return redirect('home:my_cart')
    else:
        if discounted_price > 0:
            actual_total = discounted_price
        else:
            actual_total = price
        data = Cart.objects.create(
            username = user,
            slug = slug,
            quantity = 1,
            total = actual_total,
            items = Item.objects.filter(slug= slug)[0]
        )
        data.save()
        return redirect('home:my_cart')       


class CartView(BaseView):
    def get(self, request):
        user = request.user.username
        carts = Cart.objects.filter(username= user, checkout= False)
        self.views['cart_product'] = carts
        totals = 0
        shipping_cost = 100
        for each in carts:
            totals += each.total
        self.views['total_price'] = totals
        if totals == 0:
            shipping_cost = 0
            self.views['grand_total'] = 0
        else:
            self.views['grand_total'] = totals + shipping_cost
        self.views['shipping'] = shipping_cost
        self.views['cart_count'] = Cart.objects.filter(username=user, checkout=False).count()
        return render(request, 'cart.html', self.views)


def delete_cart(request,slug):
    if Cart.objects.filter(slug = slug).exists():
        username = request.user.username
        Cart.objects.filter(username=username, slug=slug, checkout=False).delete()
    return redirect('home:my_cart')


def delete_single_cart(request,slug):
    if Cart.objects.filter(slug = slug).exists():
        username = request.user.username
        price = Item.objects.get(slug=slug).price
        discounted_price = Item.objects.get(slug=slug).discounted_price
        quantity = Cart.objects.get(username = username, slug = slug, checkout = False).quantity
        qty = quantity - 1
        if discounted_price > 0:
            actual_total = discounted_price * qty
        else:
            actual_total = price * qty
        Cart.objects.filter(username=username, slug=slug, checkout=False).update(quantity= qty, total= actual_total)
    return redirect('home:my_cart')


def checkout(request):
    if request.method == "POST":
        username = request.user.username,
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        address = request.POST['address']
        country = request.POST['country']
        city = request.POST['city']
        if fname and lname and email != "":
            data = Checkout.objects.create(
                username = username,
                fname = fname,
                lname = lname,
                email = email,
                mobile_no = mobile_no,
                address = address,
                country = country,
                city = city,
            )
            data.save()
            return redirect('/')
        else:
            messages.error(request, 'Field must not be empty')
            return redirect('home:checkouts')
    return redirect('home:checkouts')

class CheckoutView(BaseView):
    def get(self, request):
        user = request.user.username
        carts = Cart.objects.filter(username= user, checkout= False)
        self.views['cart_product'] = carts
        totals = 0
        shipping_cost = 100
        for each in carts:
            totals += each.total
        self.views['total_price'] = totals
        if totals == 0:
            shipping_cost = 0
            self.views['grand_total'] = 0
        else:
            self.views['grand_total'] = totals + shipping_cost
        self.views['shipping'] = shipping_cost
        return render(request, 'checkout.html', self.views)


# # ------------------------------------------------API----------------------------------------------------
# from .serializers import *
# from django.contrib.auth.models import User
# from .serializers import ItemSerializer
# from rest_framework import generics
# from rest_framework.filters import OrderingFilter,SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend
#
# # ViewSets define the view behavior.
#
# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#
#
# class ItemListView(generics.ListAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
#     filter_fields = ["id", "category", "label", "brand"]
#     ordering_field = ["id", "price", "name"]
#     search_fields = ["name","discription"]