# Generated by Django 3.1.7 on 2021-05-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_remove_cart_all_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='all_total',
            field=models.IntegerField(default=0),
        ),
    ]
