# Generated by Django 3.1.7 on 2021-07-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_cart_shipping_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='fname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='lname',
            field=models.CharField(max_length=200),
        ),
    ]
