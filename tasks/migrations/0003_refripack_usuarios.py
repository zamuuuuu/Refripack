# Generated by Django 3.2 on 2024-10-02 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_datedcompleted_task_datecompleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refripack',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('Tipo', models.CharField(max_length=100, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('Correo', models.EmailField(max_length=254, unique=True, verbose_name='Correo')),
                ('Telefono', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('Direccion', models.CharField(max_length=300, verbose_name='Dirección')),
            ],
        ),
    ]
