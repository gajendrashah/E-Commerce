# Generated by Django 4.1 on 2022-08-14 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_alter_product_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='banner/')),
                ('desc', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('banner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.banner')),
                ('slider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.slider')),
            ],
        ),
    ]