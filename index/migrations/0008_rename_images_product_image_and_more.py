# Generated by Django 4.1.3 on 2022-12-03 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_alter_order_transaction_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='names',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prices',
            new_name='price',
        ),
    ]
