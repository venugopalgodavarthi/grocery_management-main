# Generated by Django 5.0 on 2023-12-12 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_rename_product_category_category_items_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_item',
            name='img',
            field=models.ImageField(default='items/xyz.jpeg', upload_to='items/'),
            preserve_default=False,
        ),
    ]
