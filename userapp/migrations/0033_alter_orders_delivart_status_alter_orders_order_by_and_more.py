# Generated by Django 4.1 on 2022-08-27 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0032_alter_customers_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivart_status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('APPROVED', 'APPROVED'), ('CANCLE', 'CANCLE'), ('DISPATCHED', 'DISPATCHED'), ('RECIVED', 'RECIVED')], default='NEW', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment',
            field=models.CharField(choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID')], default='UNPAID', max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='cart',
        ),
    ]