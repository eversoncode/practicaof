from django.db import models

# Create your models here.
class cliente(models.Model):
    pk_cliente = models.AutoField(primary_key=True, blank=False,null=False,)
    nombre = models.CharField(max_length=80, null=False, blank=False)
    Dpi = models.BigIntegerField(null=False, blank=False)
    Edad = models.CharField(max_length=2, null=False, blank=False)
    direccion = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)


class mascota(models.Model):
    pk_mascota = models.AutoField(primary_key=True, blank=False, null=False,)
    tipo = models.CharField(max_length=40, null=False, blank=False)
    raza = models.CharField(max_length=200, null=False, blank=False)
    edad = models.BigIntegerField(null=False, blank=False)
    vacunas = models.BigIntegerField(null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'mascota'
        verbose_name_plural = 'mascotas'
        ordering = ['tipo']

    def __str__(self):
        return "{0}".format(self.tipo)


class cita(models.Model):
    pk_cita = models.AutoField(primary_key=True, blank=False,null=False,)
    fk_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, null=False, blank=False)
    fk_mascota = models.ForeignKey(mascota, on_delete=models.CASCADE, null=False, blank=False)
    fecha_y_hora = models.DateTimeField(null=False, blank=False)

    class Meta:
        verbose_name = 'cita'
        verbose_name_plural = 'citas'
        ordering = ['fecha_y_hora']

    def __str__(self):
        return "{0}".format(self.fecha_y_hora)
