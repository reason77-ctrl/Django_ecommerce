# Generated by Django 3.1.7 on 2021-04-01 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_feedback_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.brand'),
        ),
    ]
