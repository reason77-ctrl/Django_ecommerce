from django.db import models

STATUS = (
    ('active', 'active'),
    ('', 'default')
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
    slog = models.CharField(max_length= 100)
    status = models.CharField(choices= STATUS, max_length= 200)
    def __str__(self):
        return self.name

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
    price = models.IntegerField()
    discounted_price = models.IntegerField(default= 0)
    label = models.CharField(choices= LABEL, max_length= 200)
    image = models.ImageField(upload_to= 'media')
    status = models.CharField(max_length= 200, choices= STATUS)
    slog = models.CharField(max_length= 200)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    def __str__(self):
        return self.title
