# Generated by Django 5.1 on 2024-08-22 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mrp',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='weekly_sale',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='variantdata',
            name='quantity',
            field=models.CharField(max_length=50),
        ),
    ]
