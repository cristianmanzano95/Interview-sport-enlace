from django.db import models


# Create your models here.

class Users(models.Model):
    nombre = models.CharField(max_length=30)
    cedula = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    perfil = models.CharField(max_length= 10)
    class Meta:
        verbose_name = "cliente"

class Tokens(models.Model):
    token = models.CharField(max_length=250)
    user = models.ForeignKey(Users,on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = "token"

class Cars(models.Model):
    fecha = models.DateField(null=True)
    color = models.CharField(max_length=15)
    modelo = models.CharField(max_length=30)
    class Meta:
        verbose_name = "carro"

