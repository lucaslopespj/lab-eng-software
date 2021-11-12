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

class LoteLiberarView(UpdateView):
    model = models.Lote
    form_class = forms.LoteLiberarForm
    template_name = 'lote_liberar.html'

class LoteLanceView(UpdateView):
    model = models.Lote
    form_class = forms.LoteUpdateForm
    template_name = 'lote_lance.html'

class LoteEditarView(UpdateView):
    model = models.Lote
    form_class = forms.LoteEditarForm
    template_name = 'lote_editar.html'

class LoteEditarAdmView(UpdateView):
    model = models.Lote
    form_class = forms.LoteEditarAdmForm
    template_name = 'lote_editar_leiloeiro.html'

class LoteFinalizarLeilaoView(UpdateView):
    model = models.Lote
    form_class = forms.LoteFinalizarLeilaoForm
    template_name = 'lote_finalizar.html'

class LoteCancelView(DeleteView):
    model = models.Lote
    template_name = 'lote_cancel.html'
    success_url = '/'

class AreaExclusivaView(FormView): #Formulario para Gerar Relatório
    form_class = forms.gerarRelatorio
    template_name = 'area_exclusiva.html'
    success_url = 'relatorio'

class RelatorioView(ListView): #View para exibir relatorio
    model = models.Pagamento
    template_name = 'relatorio.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data_inicio_relatorio'] = forms.data_inicio_relatorio
        context['data_final_relatorio'] = forms.data_final_relatorio
        return context

class SaldoUpdateView(FormView):
    form_class = forms.saldoUpdateForm
    template_name = 'saldo_update.html'
    success_url = '/'

class SaldoCheckView(ListView):
    model = models.Saldo
    template_name = 'saldo_list.html'