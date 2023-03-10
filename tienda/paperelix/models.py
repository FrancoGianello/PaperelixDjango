from django.db import models
import random
# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=200)
    
    def __str__ (self):
        return self.nombre
    def getAll():
        return Categoria.objects.all()

class Producto(models.Model):
    nombre=models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='productos', null=False, blank=False, default='productos/paperelix.png')
    descripcion=models.TextField()
    materiales=models.TextField()
    medidas=models.CharField(max_length=200)
    aviso=models.TextField()
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    
    def __str__ (self):
        return (f'{self.nombre} ({self.categoria})')    
    
    def relacionados(cate, nb):
        return Producto.objects.filter(categoria=cate).exclude(nombre=nb)[:3]