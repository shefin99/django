# Generated by Django 4.1.3 on 2022-12-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_remove_product_offers_product_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]