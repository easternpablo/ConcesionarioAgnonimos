# Generated by Django 2.2.5 on 2019-11-25 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20191125_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='proveedor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Proveedor'),
        ),
    ]
