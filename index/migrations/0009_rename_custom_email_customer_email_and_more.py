# Generated by Django 4.1.3 on 2022-12-03 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_rename_images_product_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='custom_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='custom_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='custom_user',
            new_name='user',
        ),
    ]
