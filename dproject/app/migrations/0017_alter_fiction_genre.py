# Generated by Django 5.0.4 on 2024-04-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_fiction_options_fiction_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiction',
            name='genre',
            field=models.TextField(choices=[('horror', 'horror'), ('romance', 'romance'), ('crime', 'crime'), ('Dark fantasy', 'Dark fantasy')], max_length=300),
        ),
    ]
