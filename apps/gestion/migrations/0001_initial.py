# Generated by Django 3.1.7 on 2021-04-18 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=30)),
                ('tarifa_gs', models.FloatField()),
                ('tarifa_ds', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=60)),
                ('estado_final', models.CharField(max_length=15)),
                ('costo', models.FloatField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.area')),
            ],
        ),
    ]
