from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id")
    nombre = models.CharField(max_length=255,verbose_name="nombre")
    clave = models.CharField(max_length=255,verbose_name="clave")
    
    