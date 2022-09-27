# Generated by Django 4.1 on 2022-08-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_remove_events_banner_remove_events_slider_and_more'),
    ]

    operations = [
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
            field=models.ManyToManyField(blank=True, to='userapp.banner'),
        ),
        migrations.AddField(
            model_name='events',
            name='slider',
            field=models.ManyToManyField(blank=True, to='userapp.slider'),
        ),
    ]