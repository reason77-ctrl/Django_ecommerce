# Generated by Django 3.1.7 on 2021-05-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_cart_all_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='all_total',
            field=models.IntegerField(default=0),
        ),
    ]