# Generated by Django 3.0.6 on 2020-12-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='coordinates',
            field=models.FloatField(default=0, verbose_name='Координаты'),
        ),
    ]
