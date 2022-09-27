# Generated by Django 4.1 on 2022-08-15 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0019_rename_events_events_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='events',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='userapp.events'),
        ),
    ]