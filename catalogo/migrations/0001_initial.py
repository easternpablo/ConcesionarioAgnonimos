from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('coche_id', models.AutoField(primary_key=True, serialize=False)),
                ('matricula', models.CharField(max_length=7)),
                ('modelo', models.CharField(max_length=50)),
                ('kilometros', models.IntegerField(validators=[django.core.validators.MinValueValidator(500)])),
                ('color', models.CharField(max_length=50)),
                ('motor', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('caballos', models.IntegerField(validators=[django.core.validators.MinValueValidator(60)])),
                ('cilindradas', models.IntegerField()),
                ('precio', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000)])),
                ('vendido', models.BooleanField(default=False)),
                ('imagen', models.ImageField(upload_to='imagenes/Coches/')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('empleado_id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('puesto', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('proveedor_id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('taller_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('venta_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Cliente')),
                ('coche_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Coche')),
                ('empleado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='imagenes/Marcas/')),
                ('taller_id', models.ManyToManyField(to='catalogo.Taller')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('compra_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('coche_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Coche')),
                ('empleado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Empleado')),
                ('proveedor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='coche',
            name='marca_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Marca'),
        ),
    ]
