# Generated by Django 3.1.7 on 2021-05-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_carttotal_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='carttotal',
            name='checkout',
            field=models.BooleanField(default=False),
        ),
    ]