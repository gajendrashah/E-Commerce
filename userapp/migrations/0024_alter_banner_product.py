# Generated by Django 4.1 on 2022-08-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0023_remove_events_banner_banner_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='pros', to='userapp.product'),
        ),
    ]