from django.db import models

# Create your models here.
class UsuariosTareas(models.Model):
    idUsuario = models.AutoField(primary_key=True,verbose_name="Id")
    nombreUsuario = models.CharField(max_length=255,verbose_name="Usuario")
    claveUsuario = models.CharField(max_length=255,verbose_name="Contraseña")
    def __str__(self):
        fila = "Id: " +str(self.idUsuario)+ ",Nombre:" + self.nombreUsuario
        return fila
    empAuth_objects = models.Manager()