# Generated by Django 3.1.7 on 2021-08-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0059_auto_20210724_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='mobile_no',
            field=models.CharField(max_length=50),
        ),
    ]
