from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

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