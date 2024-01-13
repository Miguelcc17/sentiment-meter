from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    correo_electronico = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)

class Datos(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.TextField()
    sentimiento = models.CharField(max_length=255)
    emoción = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
