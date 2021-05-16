# Generated by Django 3.1.7 on 2021-05-10 01:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion', '0001_initial'),
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('ruc', models.CharField(default='000000-0', max_length=15)),
                ('direccion', models.CharField(default='FPUNA', max_length=100)),
                ('telefono', models.CharField(default='0981111111', max_length=20)),
                ('rubro', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=80)),
                ('monto', models.FloatField()),
                ('horas_presupuestadas', models.IntegerField(default=0)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('horas_ejecutadas', models.IntegerField(default=0, null=True)),
                ('gastos', models.FloatField(default=0)),
                ('rentabilidad_horas', models.FloatField(default=1, null=True)),
                ('rentabilidad_presupuesto', models.FloatField(default=1, null=True)),
                ('estado', models.CharField(default='Activo', max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.cliente')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='EquipoProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=40, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=80, null=True)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.contrato')),
                ('lider_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('horas_totales', models.IntegerField(null=True)),
                ('total', models.FloatField(null=True)),
                ('porcentaje_ganancia', models.DecimalField(decimal_places=3, default=0.0, max_digits=5)),
                ('ganancia_esperada', models.FloatField(null=True)),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('A', 'Aceptado'), ('R', 'Rechazado')], default='P', max_length=20)),
                ('fecha_aceptacion', models.DateField(default=None, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.area')),
                ('gerente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroHora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('detalle', models.CharField(max_length=250)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField(default=datetime.time(0, 0))),
                ('hora_fin', models.TimeField(default=datetime.time(0, 0))),
                ('horas_trabajadas', models.CharField(default='00:00', help_text='Horas trabajadas en formato HH:MM', max_length=8, null=True)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.contrato')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='PropuestaDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=500)),
                ('horas_servicio', models.IntegerField()),
                ('tarifa', models.FloatField()),
                ('total', models.FloatField()),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.cargo')),
                ('propuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='proyectos.propuesta')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='MiembroEquipoProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('LPR', 'Lider del Proyecto'), ('CON', 'Consultor'), ('AUD', 'Auditor')], default='CON', max_length=3)),
                ('tarifa_asignada', models.FloatField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.empleado')),
                ('equipo_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.equipoproyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividades', models.CharField(max_length=200)),
                ('horas_asignadas', models.IntegerField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.contrato')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.empleado')),
            ],
        ),
        migrations.AddField(
            model_name='contrato',
            name='propuesta',
            field=models.ForeignKey(limit_choices_to={'estado': 'A'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyectos.propuesta'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='tipo_servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.servicio'),
        ),
        migrations.CreateModel(
            name='CondicionPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('porcentaje_pago', models.IntegerField()),
                ('monto_pagar', models.FloatField()),
                ('fecha_estimada', models.DateField()),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.contrato')),
            ],
        ),
    ]
