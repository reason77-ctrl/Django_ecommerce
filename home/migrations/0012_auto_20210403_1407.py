# Generated by Django 3.1.7 on 2021-04-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210403_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sub_image1',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sub_image2',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sub_image3',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
