# Generated by Django 3.1.7 on 2021-04-02 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_item_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discription',
            field=models.TextField(blank=True),
        ),
    ]