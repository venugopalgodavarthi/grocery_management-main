# Generated by Django 4.1.5 on 2023-12-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_product_item_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_items',
            name='cat_img',
            field=models.ImageField(default='', upload_to='category/'),
            preserve_default=False,
        ),
    ]