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
    valor_reserva = models.DecimalField(max_digits=11, decimal_places=2)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_final = models.DateTimeField()
    valor_lance_mais_alto = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    cliente_comprador_lance_mais_alto = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cliente_vendedor')

    def __str__(self):
        return self.nome + " | " + str(self.cliente_vendedor)

    def get_absolute_url(self):
        return reverse('lote_detail', args=(str(self.id)))