from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from . import models

class LeiloeiroSignUpForm(UserCreationForm):
    nome = forms.CharField(max_length=20, required=True)
    sobrenome = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    saldo = forms.DecimalField(max_digits=6, decimal_places=2, required=True)

    class Meta(UserCreationForm.Meta):
        model = models.Leiloeiro

    @transaction.atomic
    def save(self):
        conta = super().save(commit=False)
        conta.eh_Leiloeiro = True
        conta.save()
        leiloeiro = models.Leiloeiro.objects.create(conta=conta)
        leiloeiro.nome.add(*self.cleaned_data.get('nome'))
        leiloeiro.sobrenome.add(*self.cleaned_data.get('sobrenome'))
        leiloeiro.email.add(*self.cleaned_data.get('email'))
        leiloeiro.saldo.add(*self.cleaned_data.get('saldo'))
        return conta

class ClienteSignUpForm(UserCreationForm):
    nome = forms.CharField(max_length=20, required=True)
    sobrenome = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    saldo = forms.DecimalField(max_digits=6, decimal_places=2, required=True)

    class Meta(UserCreationForm.Meta):
        model = models.Cliente

    @transaction.atomic
    def save(self):
        conta = super().save(commit=False)
        conta.eh_Cliente = True
        conta.save()
        cliente = models.Cliente.objects.create(conta=conta)
        cliente.nome.add(*self.cleaned_data.get('nome'))
        cliente.sobrenome.add(*self.cleaned_data.get('sobrenome'))
        cliente.email.add(*self.cleaned_data.get('email'))
        cliente.saldo.add(*self.cleaned_data.get('saldo'))
        return conta
