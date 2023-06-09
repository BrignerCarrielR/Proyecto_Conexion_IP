from django.db import models

from principal.opciones import Opciones
motivos = Opciones()
Bloque =motivos.Bloque()
# Create your models here.
class Switch(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=True,)
    ip = models.CharField(max_length=15, blank=False, null=False, unique=True)
    bloque = models.CharField(max_length=1, choices=Bloque, default=Bloque[0][0],
                                       blank=False, null=True)
    estado=models.BooleanField(default=False, blank=True,null=True)
    class Meta:
        verbose_name = "Switch"
        verbose_name_plural = "Switch"
        ordering = ['nombre']

    def __str__(self):
        return "{}".format(self.nombre)