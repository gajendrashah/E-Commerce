# Generated by Django 4.1 on 2022-08-14 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_banner_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='product',
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='banner/'),
        ),
        migrations.RemoveField(
            model_name='events',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='events',
            name='slider',
        ),
        migrations.AddField(
            model_name='events',
            name='banner',
            field=models.ManyToManyField(blank=True, null=True, to='userapp.banner'),
        ),
        migrations.AddField(
            model_name='events',
            name='slider',
            field=models.ManyToManyField(blank=True, null=True, to='userapp.slider'),
        ),
    ]