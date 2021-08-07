# Generated by Django 3.1.7 on 2021-05-29 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_remove_cart_all_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('carts', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.cart')),
            ],
        ),
    ]