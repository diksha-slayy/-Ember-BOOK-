# Generated by Django 5.0.4 on 2024-04-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_price_deals_discount_deals_original_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]