# Generated by Django 4.1.3 on 2022-12-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]
