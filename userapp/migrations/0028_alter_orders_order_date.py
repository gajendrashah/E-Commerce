# Generated by Django 4.1 on 2022-08-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0027_remove_orders_order_product_orders_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]