# Generated by Django 3.1.7 on 2021-04-11 22:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 4, 11, 22, 51, 16, 477071, tzinfo=utc)),
        ),
    ]
