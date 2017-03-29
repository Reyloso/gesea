# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 23:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0004_auto_20170328_1856'),
        ('inscripcion', '0007_auto_20170314_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsistenciaEstudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asistencia', models.DateTimeField(default=datetime.datetime(2017, 3, 28, 23, 56, 41, 440229, tzinfo=utc))),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripcion.Estudiantes')),
                ('programacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programacion.Programacion')),
            ],
            options={
                'verbose_name': 'Asistencia Estudiante',
                'verbose_name_plural': 'Asistencias Estudiantes',
            },
        ),
        migrations.AlterModelOptions(
            name='inscripcion',
            options={'verbose_name': 'Inscripcion individual', 'verbose_name_plural': 'Estudiantes Inscritos'},
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='fecha_inscripcion',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='programacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='programacion.Programacion'),
        ),
    ]
