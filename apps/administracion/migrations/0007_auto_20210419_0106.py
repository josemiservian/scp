# Generated by Django 3.1.7 on 2021-04-19 01:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0006_auto_20210418_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 4, 19, 1, 6, 11, 230617, tzinfo=utc)),
        ),
    ]
