# Generated by Django 4.1 on 2022-08-14 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0018_remove_events_events_events_events'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='events',
            new_name='product',
        ),
    ]
