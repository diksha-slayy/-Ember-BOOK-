# Generated by Django 5.0.4 on 2024-04-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_new_arrivals_alter_food_options_remove_food_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_arrivals',
            name='description',
        ),
        migrations.AddField(
            model_name='new_arrivals',
            name='about',
            field=models.CharField(default='About', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='new_arrivals',
            name='published_date',
            field=models.DateField(),
        ),
    ]
