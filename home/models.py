from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


STATUS = (
    ('active', 'active'),
    ('inactive', 'inactive')
)
LABEL = (
    ('new', 'new'),
    ('hot', 'hot'),
    ('sale', 'sale'),
    ('', 'default')
)
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 200)
    image = models.CharField(max_length= 200)
    slug = models.CharField(max_length= 100, unique= True)
    status = models.CharField(choices= STATUS, max_length= 200)
    def __str__(self):
        return self.name

    def get_cat_url(self):
        return reverse("home:category", kwargs = {'slug':self.slug})

class Slider(models.Model):
    name = models.CharField(max_length= 300)
    image = models.ImageField(upload_to= 'media')
    discription = models.TextField(blank= True)
    status = models.CharField(choices=STATUS, max_length=200)
    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length= 200)
    rank = models.IntegerField()
    image = models.ImageField(upload_to= 'media')
    discription = models.TextField(blank= True)
    status = models.CharField(choices=STATUS, max_length=200)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length= 200)
    image = models.ImageField(upload_to= 'media')
    status = models.CharField(choices=STATUS, max_length=200)
    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length= 200)
    name = models.CharField(max_length= 200, blank= True)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default= 0)
    label = models.CharField(choices= LABEL, max_length= 200)
    image = models.ImageField(upload_to= 'media')
    status = models.CharField(max_length= 200, choices= STATUS)
    slug = models.CharField(max_length= 200, unique= True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE, null= True)
    discription = models.TextField(blank= True)
    specification = models.TextField(blank= True)
    def __str__(self):
        return self.name
    def get_item_url(self):
        return reverse("home:products", kwargs = {'slug':self.slug})
    def get_cart_url(self):
        return reverse("home:cart", kwargs = {'slug':self.slug})

class Feedback(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length= 200)
    profession = models.CharField(max_length= 100)
    discription = models.TextField()
    status = models.CharField(max_length=200, choices=STATUS, blank= True)
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length= 200)
    email = models.EmailField(max_length= 200, blank= True)
    subject = models.CharField(max_length= 500, blank= True)
    message = models.TextField()
    def __str__(self):
        return self.name

class Review(models.Model):
    username = models.CharField(max_length= 250, blank= True)
    date = models.DateField(auto_now_add= True)
    email = models.EmailField(max_length= 250, blank=True)
    review = models.TextField(blank= True)
    rating = models.IntegerField()
    slug = models.CharField(max_length= 200, blank= True)
    status = models.CharField(choices= STATUS,max_length= 200, default= 'active')

    def __str__(self):
        return self.username

class Cart(models.Model):
    username = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    items = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
    quantity = models.IntegerField()
    total = models.IntegerField(default=0)
    all_total = models.IntegerField(default=0)
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Checkout(models.Model):
    username = models.CharField(max_length=300)
    fname = models.CharField(max_length=200, blank=True)
    lname = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=300,blank=True)
    mobile_no = models.CharField(max_length=50)
    address = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.username