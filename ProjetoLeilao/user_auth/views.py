from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from . import forms

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = forms.SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
