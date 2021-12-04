from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Lote(models.Model):
    cliente_vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    estado_conservacao = models.TextField(
        choices=[('VELHO', 'VELHO'),
                 ('SEMINOVO', 'SEMINOVO'),
                 ('NOVO', 'NOVO')],
        default='VELHO',
    )
    autor = models.CharField(max_length=200, default="Autor")
    editora = models.CharField(max_length=200, default="Editora")
    numero_de_paginas = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    valor_minimo_lance = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    valor_minimo_incremento_por_lance = models.DecimalField(max_digits=11, decimal_places=2, default=0.01)
    valor_reserva = models.DecimalField(max_digits=11, decimal_places=2)
    data_inicio = models.DateTimeField()
    data_final = models.DateTimeField(null = True)
    valor_lance_mais_alto = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    cliente_comprador_lance_mais_alto = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cliente_vendedor')
    taxa_comissao = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    numero_de_lances = models.DecimalField(max_digits=11, decimal_places=0, default=0)
    liberado_para_lances = models.BooleanField(default=False)
    leilao_finalizado = models.BooleanField(default=False)
    lote_foi_vendido = models.BooleanField(default=False)

    def __str__(self):
        return self.nome + " | " + str(self.cliente_vendedor)

    def get_absolute_url(self):
        return '/lote/%i/' % self.id

class Saldo(models.Model): #Saldo disponivel para cliente(comprador/vendedor)
    username_cliente = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return str(self.cliente)

class Pagamento(models.Model): #Comissoes pagas ao leilao, usadas para gerar Relatorio de Faturamento
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, null=True)
    valor = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    data = models.DateTimeField()
    tipo_de_pagamento = models.TextField(
        choices=[('COMISSÃO NOVO LOTE', 'COMISSÃO NOVO LOTE'),
                 ('COMISSÃO LANCE', 'COMISSÃO LANCE')],
        default='COMISSÃO NOVO LOTE',
    )

    def __str__(self):
        return str(self.valor) + " " + str(self.data)