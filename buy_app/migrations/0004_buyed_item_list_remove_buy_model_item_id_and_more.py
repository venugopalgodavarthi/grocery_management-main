# Generated by Django 4.2.7 on 2023-12-13 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy_app', '0003_remove_buy_model_t_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyed_item_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_id', models.PositiveBigIntegerField()),
                ('item_id', models.PositiveBigIntegerField()),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='buy_model',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='buy_model',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='buy_model',
            name='quantity',
        ),
        migrations.AddField(
            model_name='buy_model',
            name='total_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
