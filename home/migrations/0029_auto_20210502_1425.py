# Generated by Django 3.1.7 on 2021-05-02 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20210502_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carttotal',
            name='sub_total',
        ),
        migrations.AddField(
            model_name='carttotal',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.cart'),
        ),
        migrations.AddField(
            model_name='carttotal',
            name='checkout',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='carttotal',
            name='grand_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carttotal',
            name='net_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carttotal',
            name='shipping_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carttotal',
            name='slug',
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='carttotal',
            name='username',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
