# Generated by Django 5.0.4 on 2024-04-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_fiction'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiction',
            name='genre',
            field=models.TextField(default='love and horror', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fiction',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fiction',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]