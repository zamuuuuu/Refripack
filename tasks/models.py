from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre



class Refripack(models.Model):
    id = models.AutoField(primary_key=True)  
    Nombre = models.CharField(max_length=200, verbose_name='Nombre')
    Tipo = models.CharField(max_length=100, verbose_name='Tipo')

    def __str__(self):
        return self.Nombre


class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=200, verbose_name='Nombre')
    Correo = models.EmailField(max_length=254, unique=True, verbose_name='Correo')
    Telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    Direccion = models.CharField(max_length=300, verbose_name='Dirección')

    def __str__(self):
        return self.Nombre

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Agrega otros campos necesarios para los productos

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Cart(models.Model):
    items = models.ManyToManyField(CartItem)

    @property
    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)  # Este campo debe existir
    # Agrega otros campos si es necesario

    def __str__(self):
        return self.title



