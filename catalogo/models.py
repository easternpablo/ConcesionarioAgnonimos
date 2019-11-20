from django.db import models
from django.core.validators import MinValueValidator

class Marca(models.Model):
    marca_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="imagenes/Marcas/")

    def __str__(self):
        return f"{self.nombre}"

class Coche(models.Model):
    coche_id =  models.AutoField(primary_key=True)
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
    imagen = models.ImageField(upload_to="imagenes/Coches/")

    def __str__(self):
        return f"{self.matricula} -> {self.modelo}"