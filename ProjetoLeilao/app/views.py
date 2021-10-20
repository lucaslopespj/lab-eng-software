from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from django.contrib.auth import login
from django.core.mail import send_mail
from . import forms
from . import models

class LeiloeiroSignUpView(CreateView):
    model = models.Leiloeiro
    form_class = forms.LeiloeiroSignUpForm
    template_name = 'leiloeiro_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'leiloeiro'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        send_mail(
            'ProjetoLeilão PCS3643 - Confirmação de cadastro',
            'Olá, ' + form.nome + ' esse email foi enviado para confirmar seu cadastro como Leiloeiro em nosso site :)',
            'nazter57@usp.br',
            [form.email],
            fail_silently=False,
        )
        login(self.request, user)
        return redirect('home')


class ClienteSignUpView(CreateView):
    model = models.Cliente
    form_class = forms.ClienteSignUpForm
    template_name = 'cliente_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'cliente'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        send_mail(
            'ProjetoLeilão PCS3643 - Confirmação de cadastro',
            'Olá, ' + form.nome + ' esse email foi enviado para confirmar seu cadastro como Cliente em nosso site :)',
            'nazter57@usp.br',
            [form.email],
            fail_silently=False,
        )
        login(self.request, user)
        return redirect('home')

class SignUpView(TemplateView):
    template_name = 'signup.html'

class Home(TemplateView):
    template_name = 'home.html'