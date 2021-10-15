from django.db import models

from django.urls import reverse

class Comprador(models.Model):
    nome = models.CharField(max_length = 200)
    cpf = models.DecimalField(max_digits=11, decimal_places=0)
    bio = models.TextField()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('comprador_detail', args=[str(self.id)])

class Leiloeiro(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.DecimalField(max_digits=11, decimal_places=0)
    bio = models.TextField()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('leiloeiro_detail', args=[str(self.id)])

class Vendedor(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.DecimalField(max_digits=11, decimal_places=0)
    bio = models.TextField()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('vendedor_detail', args=[str(self.id)])

class Lote(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    estadoConservacao = models.TextField(
        choices = [('VELHO', 'VELHO'),
                   ('SEMINOVO', 'SEMINOVO'),
                   ('NOVO', 'NOVO')],
        default = 'VELHO',
    )
    estadoVenda = models.TextField(
        choices = [('VENDIDO', 'VENDIDO'),
                   ('NAO VENDIDO', 'NÃO VENDIDO')],
        default = 'NAO VENDIDO',
    )
    valorReserva = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('lote_detail', args=[str(self.id)])

class Notificacao(models.Model):
    texto = models.TextField()

    def __str__(self):
        return self.texto

class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    data = models.TimeField()

    def __str__(self):
        return self.data

class ofertado(models.Model):#RELACIONAMENTO 1 Lote, 1 Vendedor
    vendedor = models.OneToOneField(
        Vendedor,
        on_delete=models.CASCADE,
    )

    lote = models.OneToOneField(
        Lote,
        on_delete=models.CASCADE,
    )

class destinatario(models.Model):#RELACIONAMENTO 1 Notificação, 1 Vendedor
    vendedor = models.OneToOneField(
        Vendedor,
        on_delete=models.CASCADE,
    )

    notificacao = models.OneToOneField(
        Notificacao,
        on_delete=models.CASCADE,
    )

class Catalogo(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class OfertaLotesDeProduto(models.Model):

    def cadastarLote(self, vendedor, lote, notificacao, pagamento):
        return "Work in Progress..."

    def __str__(self):
        return "Ofertar Lotes de Produtos"

class Leilao(models.Model):
    nome = models.CharField(max_length=200)
    valorMinimoLance = models.DecimalField(max_digits=11, decimal_places=2)
    incrementoPorLance = models.DecimalField(max_digits=11, decimal_places=2)
    dataInicio = models.TimeField()
    dataFinal = models.TimeField()

    def __str__(self):
        return self.nome

class listado(models.Model): #RELACIONAMENTO 1 Leilao, 1 Catalogo
    catalogo = models.OneToOneField(
        Catalogo,
        on_delete=models.CASCADE,
    )

    leilao = models.OneToOneField(
        Leilao,
        on_delete=models.CASCADE,
    )

class RealizaLeilao(models.Model):

    def atualizarCatalogo(self, Catalogo, Leilao):
        return "Work in Progress..."
    def liberarLote(self, Lote, Leilao):
        return "Work in Progress..."
    def terminarLeilao(self, Leilao):
        return "Work in Progress..."
    def realizarLance(self, Lance, Leilao):
        return "Work in Progress..."
    def efetuarPagamento(self, Leilao):
        return "Work in Progress..."

    def __str__(self):
        return "Realizar Leilão"

class GeracaoDeRelatorio(models.Model):

    def gerarRelatorio(self, dataInicio, dataFinal, tipooRelatorio):
        return "Work in Progress..."

    def __str__(self):
        return "Gerar Relatório"

class Lance(models.Model):
    valor = models.DecimalField(max_digits=11, decimal_places=2)

class realizado(models.Model): #RELACIONAMENTO 1 Lance, 1 Comprador
    lance = models.OneToOneField(
        Lance,
        on_delete=models.CASCADE,
    )

    comprador = models.OneToOneField(
        Comprador,
        on_delete=models.CASCADE,
    )
