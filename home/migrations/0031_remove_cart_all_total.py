# Generated by Django 3.1.7 on 2021-05-19 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20210513_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='all_total',
        ),
    ]