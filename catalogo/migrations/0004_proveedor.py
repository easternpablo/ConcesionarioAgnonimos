# Generated by Django 2.2.5 on 2019-11-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_empleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('proveedor_id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
