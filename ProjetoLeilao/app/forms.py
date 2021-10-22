from django import forms
from . import models

class LoteCreateForm(forms.ModelForm): #Ofertar lote de produtos
    class Meta:
        model = models.Lote
        fields = ('nome', 'descricao', 'estado_conservacao', 'valor_reserva', 'cliente_vendedor', 'data_final')
        widgets = { #elementos HTML correspondentes aos campos
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_conservacao': forms.Select(attrs={'class': 'form-control'}),
            'valor_reserva': forms.NumberInput(attrs={'class': 'form-control'}),
            'cliente_vendedor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'cliente_vendedor_field', 'type': 'hidden'}),
            'data_final': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

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
        lance_formulario = self.cleaned_data['valor_lance_mais_alto']
        lance_atual = self.instance.valor_lance_mais_alto
        if( lance_formulario < lance_atual):
            raise forms.ValidationError('Você precisa oferecer mais que o lance mais alto atual (' + str(lance_atual) + ')')
