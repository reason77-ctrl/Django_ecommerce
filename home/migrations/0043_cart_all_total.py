# Generated by Django 3.1.7 on 2021-06-05 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20210605_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='all_total',
            field=models.IntegerField(default=0),
        ),
    ]