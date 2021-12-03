from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from app import models

TIPOS_DE_USUARIOS = [
    ('leiloeiro', 'Leiloeiro'),
    ('cliente', 'Cliente'),
]

class SignUpForm(UserCreationForm):
    first_name = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=TIPOS_DE_USUARIOS,
    )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')
    def clean(self):
        #PRIMEIRA VALIDACAO: nao pode enviar formulario sem first name
        if(not self.cleaned_data.get('first_name')):
            raise forms.ValidationError('Você precisa selecionar um First name')
        # SEGUNDA VALIDACAO: nao pode enviar formulario com dois first name
        first_name_form = self.cleaned_data['first_name']
        if(str(first_name_form) == "['leiloeiro', 'cliente']"):
            raise forms.ValidationError('Você precisa selecionar apenas um First name')
        # vamos criar model de Saldo para cliente
        if(str(first_name_form) == "['cliente']"):
            saldo = models.Saldo(username_cliente=self.cleaned_data['username'], valor=0)
            saldo.save()