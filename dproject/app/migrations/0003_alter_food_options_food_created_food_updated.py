# Generated by Django 5.0.4 on 2024-04-11 11:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_food_joined_date_food_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='food',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
