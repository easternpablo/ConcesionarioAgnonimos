from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Marca(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    imagen = models.ImageField(upload_to="imagenes/Marcas/")
    taller_id = models.ManyToManyField('Taller')

    def __str__(self):
        return f"{self.nombre}"

    def get_url_marca(self):
        return "/concesionario/marcas/"+self.nombre+"/"
        
class Coche(models.Model):
    coche_id = models.AutoField(primary_key=True)
    marca_id = models.ForeignKey('Marca', on_delete=models.CASCADE)
    matricula = models.CharField(max_length=7)
    modelo = models.CharField(max_length=50)
    kilometros = models.IntegerField(validators=[MinValueValidator(500)])
    color = models.CharField(max_length=50)
    motor = models.CharField(max_length=50) # Ej: Diesel, Gasolina, Electrico,...
    tipo = models.CharField(max_length=50)  # Ej: Turismo, Monovolumen, TodoTerreno,...
    caballos = models.IntegerField(validators=[MinValueValidator(60)])
    cilindradas = models.IntegerField()
    precio = models.IntegerField(validators=[MinValueValidator(1000)])
    vendido = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to="imagenes/Coches/")
    
    def __str__(self):
        return f"{self.marca_id} -> {self.modelo}"

class Taller(models.Model):
    taller_id =  models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=100) 
    email = models.EmailField(max_length=50) 
  
    def __str__(self):
        return f"{self.nombre} -> {self.telefono}" 

class Cliente(models.Model):
    cliente_id =  models.AutoField(primary_key=True)
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=100) 
    email = models.EmailField(max_length=50) 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.dni} -> {self.nombre}"

class Empleado(models.Model):
    empleado_id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)                 #son iguales, se puede usar la misma??
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=100) 
    email = models.EmailField(max_length=50) 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    puesto = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.dni} -> {self.nombre}"   

class Proveedor(models.Model):
    proveedor_id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=100) 
    email = models.EmailField(max_length=50) 
    
    def __str__(self):
        return f"{self.dni} -> {self.nombre}" 

class Compra(models.Model):
    compra_id = models.AutoField(primary_key=True)
    coche_id = models.ForeignKey('Coche', on_delete=models.CASCADE)  
    proveedor_id = models.ForeignKey('Proveedor', on_delete=models.CASCADE) 
    empleado_id = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.coche_id} -> {self.proveedor_id} -> {self.empleado_id} -> {self.fecha}" 

class Venta(models.Model):
    venta_id = models.AutoField(primary_key=True)
    coche_id = models.ForeignKey('Coche', on_delete=models.CASCADE)
    cliente_id = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    empleado_id = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.matricula} -> {self.modelo}"