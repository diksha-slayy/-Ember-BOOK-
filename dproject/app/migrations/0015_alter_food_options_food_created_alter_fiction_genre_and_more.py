# Generated by Django 5.0.4 on 2024-04-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_fiction_genre_fiction_price_fiction_published_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='food',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fiction',
            name='genre',
            field=models.TextField(choices=[('horror', 'horror'), ('romance', 'romance'), ('crime', 'crime')], max_length=300),
        ),
        migrations.AlterField(
            model_name='food',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
