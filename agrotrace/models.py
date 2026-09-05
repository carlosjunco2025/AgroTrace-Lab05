from django.db import models

class CentroAcopio(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class VariedadCultivo(models.Model):
    nombre_cultivo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cultivo

class CertificacionAgricola(models.Model):
    nombre_certificacion = models.CharField(max_length=100)
    entidad_emisora = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_certificacion

class FundoProductor(models.Model):
    nombre_fundo = models.CharField(max_length=100)
    propietario_dni_ruc = models.CharField(max_length=20)
    hectareas = models.DecimalField(max_digits=8, decimal_places=2)
    valido_exportacion = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_fundo

class LoteRecepcionado(models.Model):
    fundo = models.ForeignKey(FundoProductor, on_delete=models.CASCADE, related_name='lotes')
    codigo_lote = models.CharField(max_length=50, unique=True)
    toneladas_brutas = models.DecimalField(max_digits=8, decimal_places=2)
    porcentaje_descarte = models.DecimalField(max_digits=5, decimal_places=2)
    estado_evaluacion = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo_lote} - {self.fundo.nombre_fundo}"