# Generated by Django 2.2.5 on 2019-12-03 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('reserva_id', models.AutoField(primary_key=True, serialize=False)),
                ('cliente_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Cliente')),
                ('coche_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Coche')),
            ],
        ),
    ]
