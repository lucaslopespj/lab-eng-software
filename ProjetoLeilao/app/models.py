from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db.models import ForeignKey

class Conta(AbstractUser):
    """
    Define tipo de usuario: Leiloeiro ou Cliente(comprador/vendedor)
    """
    eh_Leiloeiro = models.BooleanField(default = False)
    eh_Cliente = models.BooleanField(default = False)


class Leiloeiro(models.Model):
    """
    Model de usuario tipo Leiloeiro
    """
    conta = models.OneToOneField(Conta, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length = 30)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    saldo = models.DecimalField(max_digits=11, decimal_places=2)
    def __str__(self):
        return self.email


class Cliente(models.Model):
    """
    Model de usuario tipo Cliente
    """
    conta = models.OneToOneField(Conta, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=30)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    saldo = models.DecimalField(max_digits=11, decimal_places=2)
    def __str__(self):
        return self.email


class Lote(models.Model):
    """
    Model de lote de produtos
    """
    vendedor_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    descricao = models.TextField()
    estado_conservacao = models.TextField(
        choices=[('VELHO', 'VELHO'),
                 ('SEMINOVO', 'SEMINOVO'),
                 ('NOVO', 'NOVO')],
        default='VELHO',
    )
    valor_reserva = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.nome