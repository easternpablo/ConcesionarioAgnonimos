# Generated by Django 2.2.5 on 2019-11-19 18:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('marca_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='imagenes/Marcas/')),
            ],
        ),
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('coche_id', models.AutoField(primary_key=True, serialize=False)),
                ('matricula', models.CharField(max_length=7)),
                ('modelo', models.CharField(max_length=50)),
                ('kilometros', models.IntegerField(validators=[django.core.validators.MinValueValidator(500)])),
                ('motor', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('caballos', models.IntegerField(validators=[django.core.validators.MinValueValidator(60)])),
                ('cilindradas', models.IntegerField()),
                ('precio', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000)])),
                ('imagen', models.ImageField(upload_to='imagenes/Coches/')),
                ('marca_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Marca')),
            ],
        ),
    ]
