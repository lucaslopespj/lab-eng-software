from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from app.models import Lote, Saldo, Pagamento

# Create your tests here.

class LoteModelTestCase(TestCase):
    """
        Não estamos trabalhando no banco de dados da aplicação, mas sim num banco de dados de teste.
        Portanto, precisamos criar TODOS os objetos a serem usados nos testes.
    """
    @classmethod
    def setUpTestData(cls):
        usuario_vendedor = User.objects.create_user(username='VENDEDOR', password='12epusp34')
        usuario_comprador = User.objects.create_user(username='COMPRADOR', password='12epusp34')
        Lote.objects.create(nome='Esquadro de Acrilico', cliente_vendedor=usuario_vendedor, descricao='Um esquadro de acrilico para aulas de geometria ou desenho.',
                        estado_conservacao='VELHO', valor_reserva=200, data_final=timezone.now(),
                        valor_lance_mais_alto=300, cliente_comprador_lance_mais_alto=usuario_comprador)

    def teste_label_nome(self):
        field_nome = Lote._meta.get_field('nome').verbose_name
        self.assertEquals(field_nome, 'nome')

    def teste_label_cliente_vendedor(self):
        field_cliente_vendedor = Lote._meta.get_field('cliente_vendedor').verbose_name
        self.assertEquals(field_cliente_vendedor, 'cliente vendedor')

    def teste_label_descricao(self):
        field_descricao = Lote._meta.get_field('descricao').verbose_name
        self.assertEquals(field_descricao, 'descricao')

    def teste_label_estado_conservacao(self):
        field_estado_conservacao = Lote._meta.get_field('estado_conservacao').verbose_name
        self.assertEquals(field_estado_conservacao, 'estado conservacao')

    def teste_label_valor_reserva(self):
        field_valor_reserva = Lote._meta.get_field('valor_reserva').verbose_name
        self.assertEquals(field_valor_reserva, 'valor reserva')

    def teste_label_data_inicio(self):
        field_data_inicio = Lote._meta.get_field('data_inicio').verbose_name
        self.assertEquals(field_data_inicio, 'data inicio')

    def teste_label_data_final(self):
        field_data_final = Lote._meta.get_field('data_final').verbose_name
        self.assertEquals(field_data_final, 'data final')

    def teste_label_valor_lance_mais_alto(self):
        field_valor_lance_mais_alto = Lote._meta.get_field('valor_lance_mais_alto').verbose_name
        self.assertEquals(field_valor_lance_mais_alto, 'valor lance mais alto')

    def teste_label_cliente_comprador_lance_mais_alto(self):
        field_cliente_comprador_lance_mais_alto = Lote._meta.get_field('cliente_comprador_lance_mais_alto').verbose_name
        self.assertEquals(field_cliente_comprador_lance_mais_alto, 'cliente comprador lance mais alto')

    def teste_valor_nome(self):
        lote = Lote.objects.get(id = 1)
        valor_nome = '{0}'.format(lote.nome)
        self.assertEquals(valor_nome, 'Esquadro de Acrilico')

    def teste_valor_estado_conservacao(self):
        lote = Lote.objects.get(id = 1)
        valor_estado_conservacao = '{0}'.format(lote.estado_conservacao)
        self.assertEquals(valor_estado_conservacao, 'VELHO')

class SaldoModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Saldo.objects.create(username_cliente='VENDEDOR', valor=20)

    def teste_label_username_cliente(self):
        field_username_cliente = Saldo._meta.get_field('username_cliente').verbose_name
        self.assertEquals(field_username_cliente, 'username cliente')

    def teste_label_valor(self):
        field_valor = Saldo._meta.get_field('valor').verbose_name
        self.assertEquals(field_valor, 'valor')

    def teste_valor_username_cliente(self):
        saldo = Saldo.objects.get(id = 1)
        valor_username_cliente = '{0}'.format(saldo.username_cliente)
        self.assertEquals(valor_username_cliente, 'VENDEDOR')

    def teste_valor_valor(self):
        saldo = Saldo.objects.get(id = 1)
        valor_valor = '{0}'.format(saldo.valor)
        self.assertEquals(valor_valor, '20.00')

class PagamentoModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Pagamento.objects.create(valor=1)

    def teste_label_valor(self):
        field_valor = Pagamento._meta.get_field('valor').verbose_name
        self.assertEquals(field_valor, 'valor')

    def teste_label_data(self):
        field_data = Pagamento._meta.get_field('data').verbose_name
        self.assertEquals(field_data, 'data')

    def teste_valor_valor(self):
        pagamento = Pagamento.objects.get(id = 1)
        valor_valor = '{0}'.format(pagamento.valor)
        self.assertEquals(valor_valor, '1.00')
