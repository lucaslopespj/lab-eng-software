from django.db import models

from django.urls import reverse

class Leiloeiro(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.DecimalField(max_digits=11, decimal_places=0)
    bio = models.TextField()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('leiloeiro_detail', args=[str(self.id)])