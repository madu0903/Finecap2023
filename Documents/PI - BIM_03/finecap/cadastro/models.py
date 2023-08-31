from django.db import models

# Create your models here.

class Stand(models.Model):
    localizacao=models.CharField(max_length=250)
    valor=models.FloatField() 

    def __str__(self):
        return self.localizacao

class Reserva(models.Model):
    cnpj=models.CharField(max_length=50)
    nome_empresa=models.CharField(max_length=200)
    categoria_empresa=models.CharField(max_length=200)
    quitado=models.BooleanField()
    stand=models.ForeignKey(Stand, on_delete=models.CASCADE)
