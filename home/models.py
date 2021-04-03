from django.db import models
from django.urls import reverse

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
    slog = models.CharField(max_length= 100, unique= True)
    status = models.CharField(choices= STATUS, max_length= 200)
    def __str__(self):
        return self.name

    def get_cat_url(self):
        return reverse("home:category", kwargs = {'slog':self.slog})

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
    slog = models.CharField(max_length= 200, unique= True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE, null= True)
    discription = models.TextField(blank= True)
    specification = models.TextField(blank= True)
    def __str__(self):
        return self.title
    def get_item_url(self):
        return reverse("home:products", kwargs = {'slog':self.slog})

class Feedback(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length= 200)
    profession = models.CharField(max_length= 100)
    discription = models.TextField()
    status = models.CharField(max_length=200, choices=STATUS, blank= True)
    def __str__(self):
        return self.name