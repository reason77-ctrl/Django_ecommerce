# Generated by Django 3.1.7 on 2021-06-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_remove_cart_all_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='all_total',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Cart_Total',
        ),
    ]
