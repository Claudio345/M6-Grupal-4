from django.db import models
from django.utils import timezone
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    image = models.URLField(verbose_name="URL del logo")
    descuento = models.FloatField(verbose_name="Descuento")
    demora = models.IntegerField(verbose_name="Demora")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre