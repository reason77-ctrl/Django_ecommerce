# Generated by Django 3.1.7 on 2021-04-09 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user_name',
            new_name='username',
        ),
    ]
