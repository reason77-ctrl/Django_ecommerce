# Generated by Django 3.1.7 on 2021-07-24 08:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_auto_20210724_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='shipping_cost',
            field=models.PositiveIntegerField(default=100, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
