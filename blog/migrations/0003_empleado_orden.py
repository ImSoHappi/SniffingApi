# Generated by Django 2.0.9 on 2018-12-12 01:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181130_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=400)),
                ('telefono', models.CharField(max_length=9)),
                ('correo', models.CharField(blank=True, max_length=2550)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('folio', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('horainicio', models.TimeField(default=django.utils.timezone.now)),
                ('horatermino', models.TimeField()),
                ('idascensor', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('fallas', models.TextField(max_length=100)),
                ('reparaciones', models.TextField(max_length=100)),
                ('piezas', models.TextField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Cliente')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Empleado')),
            ],
        ),
    ]