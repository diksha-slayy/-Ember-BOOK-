# Generated by Django 5.0.4 on 2024-04-17 07:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_food_options_food_created_alter_fiction_genre_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fiction',
            options={'ordering': ['-updated_at', '-created_at']},
        ),
        migrations.AddField(
            model_name='fiction',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fiction',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
