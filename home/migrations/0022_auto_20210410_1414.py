# Generated by Django 3.1.7 on 2021-04-10 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210409_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='slog',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='slog',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='slog',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='slog',
            new_name='slug',
        ),
    ]
