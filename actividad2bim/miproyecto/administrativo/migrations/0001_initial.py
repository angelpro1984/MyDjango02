# Generated by Django 5.0 on 2023-12-29 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=30, unique=True)),
                ('nombres', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('titulo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('numcred', models.CharField(max_length=100)),
                ('progacad', models.CharField(max_length=100)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.docente')),
            ],
        ),
    ]