# Generated by Django 4.2.7 on 2023-12-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0002_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='age',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='session',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]