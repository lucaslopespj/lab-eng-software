from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from django.contrib.auth import login
from django.core.mail import send_mail
from . import forms
from . import models

# Create your views here

class Home(ListView):
    model = models.Lote
    template_name = 'home.html'
    ordering = ['-data_inicio']

class LoteDetailView(DetailView):
    model = models.Lote
    template_name = 'lote_detail.html'

class LoteAddView(CreateView):
    model = models.Lote
    form_class = forms.LoteCreateForm
    template_name = 'lote_add.html'

class LoteLanceView(UpdateView):
    model = models.Lote
    form_class = forms.LoteUpdateForm
    template_name = 'lote_lance.html'

class LoteCancelView(DeleteView):
    model = models.Lote
    template_name = 'lote_cancel.html'

class AreaExclusivaView(TemplateView):
    template_name = 'area_exclusiva.html'

class SaldoUpdateView(FormView):
    form_class = forms.saldoUpdateForm
    template_name = 'saldo_update.html'
    success_url = '/'

class SaldoCheckView(ListView):
    model = models.Saldo
    template_name = 'saldo_list.html'