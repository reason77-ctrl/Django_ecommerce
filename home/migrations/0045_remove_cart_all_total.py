# Generated by Django 3.1.7 on 2021-06-05 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_cart_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='all_total',
        ),
    ]