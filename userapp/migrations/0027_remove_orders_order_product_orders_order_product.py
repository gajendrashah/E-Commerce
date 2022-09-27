# Generated by Django 4.1 on 2022-08-16 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0026_alter_product_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='order_product',
        ),
        migrations.AddField(
            model_name='orders',
            name='order_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.product'),
        ),
    ]
