# Generated by Django 3.1.7 on 2021-07-24 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_auto_20210724_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='mobile_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
