from django import forms
from datetime import datetime
import pytz
from . import models

class LoteCreateForm(forms.ModelForm): #Ofertar lote de produtos
    class Meta:
        model = models.Lote
        fields = ('nome', 'descricao', 'estado_conservacao', 'valor_reserva', 'valor_minimo_lance', 'valor_minimo_incremento_por_lance', 'cliente_vendedor', 'data_final')
        widgets = { #elementos HTML correspondentes aos campos
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_conservacao': forms.Select(attrs={'class': 'form-control'}),
            'valor_reserva': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_minimo_lance': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_minimo_incremento_por_lance': forms.NumberInput(attrs={'class': 'form-control'}),
            'cliente_vendedor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'cliente_vendedor_field', 'type': 'hidden'}),
            'data_final': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
    def clean(self):#vamos calcular taxa de cancelamento
        valor_base = self.cleaned_data['valor_reserva']
        if(valor_base <= 1000):
            self.instance.taxa_cancelamento = float(valor_base) / 100.00 # taxa de 1%
        elif(valor_base <= 10000):
            self.instance.taxa_cancelamento = 2 * float(valor_base) / 50.00 # taxa de 2%
        elif(valor_base <= 50000):
            self.instance.taxa_cancelamento = 3 * float(valor_base) / 100.00  # taxa de 3%
        elif(valor_base <= 100000):
            self.instance.taxa_cancelamento = 4 * float(valor_base) / 100.00  # taxa de 4%
        else:
            self.instance.taxa_cancelamento = 5 * float(valor_base) / 100.00  # taxa de 5%
        #PRIMEIRA VALIDACAO: Leilao precisa acabar no futuro
        utc = pytz.UTC
        tempo_atual = utc.localize(datetime.now())
        tempo_final = self.cleaned_data['data_final']
        if (tempo_final < tempo_atual):
            raise forms.ValidationError('O leilão não pode acabar antes do momento atual!')



class LoteUpdateForm(forms.ModelForm): #Realizar Lance
    class Meta:
        model = models.Lote
        fields = ('valor_lance_mais_alto', 'cliente_comprador_lance_mais_alto')
        widgets = {
            'valor_lance_mais_alto': forms.NumberInput(attrs={'class': 'form-control'}),
            'cliente_comprador_lance_mais_alto': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'cliente_comprador_lance_mais_alto_field', 'type': 'hidden'}),
        }
    def clean(self):
        #PRIMEIRA VALIDACAO: Tem que ser maior que lance atual
        lance_formulario = self.cleaned_data['valor_lance_mais_alto']
        lance_atual = self.instance.valor_lance_mais_alto
        if( lance_formulario < lance_atual):
            raise forms.ValidationError('Você precisa oferecer mais que o lance mais alto atual (' + str(lance_atual) + ')')
        #SEGUNDA VALIDACAO: Tem que ser maior que lance minimo
        lance_minimo = self.instance.valor_minimo_lance
        if(lance_formulario < lance_minimo):
            raise forms.ValidationError('O valor mínimo de lance para esse lote eh ' + str(lance_minimo))
        #TERCEIRA VALIDACAO: Se ja teve lance, precisa respeitar incremento minimo
        incremento_minimo = self.instance.valor_minimo_incremento_por_lance
        if(lance_atual >= lance_minimo and lance_formulario < lance_atual + incremento_minimo):
            raise forms.ValidationError('Pela regra de incremento mínimo, você precisa ofertar pelo menos ' + str(lance_atual+incremento_minimo))
        #QUARTA VALIDACAO: Se o leilao ja expirou, nao dah pra fazer lance
        utc = pytz.UTC
        tempo_atual = utc.localize(datetime.now())
        tempo_final = self.instance.data_final
        if( tempo_final < tempo_atual ):
            raise forms.ValidationError('Infelizmente esse leilão acabou na datetime ' + tempo_final.strftime("%m/%d/%Y, %H:%M:%S"))

