from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Comprador, Leiloeiro, Vendedor

class HomeView(TemplateView):
    template_name = 'home.html'

class CompradorListView(ListView):
    model = Comprador
    template_name = 'comprador_home.html'

class CompradorDetailView(DetailView):
    model = Comprador
    template_name = 'comprador_detail.html'
    context_object_name = 'comprador'

class CompradorCreateView(CreateView):
    model = Comprador
    template_name = 'comprador_new.html'
    fields = '__all__'
    context_object_name = 'comprador'

class CompradorUpdateView(UpdateView):
    model = Comprador
    fields = ['bio'] #Only Editable Fields
    template_name = 'comprador_edit.html'
    context_object_name = 'comprador'

class CompradorDeleteView(DeleteView):
    model = Comprador
    template_name = 'comprador_delete.html'
    success_url = reverse_lazy('comprador_home')
    context_object_name = 'comprador'

class LeiloeiroListView(ListView):
    model = Leiloeiro
    template_name = 'leiloeiro_home.html'
    context_object_name = 'leiloeiro'

class LeiloeiroDetailView(DetailView):
    model = Leiloeiro
    template_name = 'leiloeiro_detail.html'
    context_object_name = 'leiloeiro'

class LeiloeiroCreateView(CreateView):
    model = Leiloeiro
    template_name = 'leiloeiro_new.html'
    fields = '__all__'
    context_object_name = 'leiloeiro'

class LeiloeiroUpdateView(UpdateView):
    model = Leiloeiro
    fields = ['bio'] #Only Editable Fields
    template_name = 'leiloeiro_edit.html'
    context_object_name = 'leiloeiro'

class LeiloeiroDeleteView(DeleteView):
    model = Leiloeiro
    template_name = 'leiloeiro_delete.html'
    success_url = reverse_lazy('leiloeiro_home')
    context_object_name = 'leiloeiro'

class VendedorListView(ListView):
    model = Vendedor
    template_name = 'vendedor_home.html'
    context_object_name = 'vendedor'

class VendedorDetailView(DetailView):
    model = Vendedor
    template_name = 'vendedor_detail.html'
    context_object_name = 'vendedor'

class VendedorCreateView(CreateView):
    model = Vendedor
    template_name = 'vendedor_new.html'
    fields = '__all__'
    context_object_name = 'vendedor'

class VendedorUpdateView(UpdateView):
    model = Vendedor
    fields = ['bio'] #Only Editable Fields
    template_name = 'vendedor_edit.html'
    context_object_name = 'vendedor'

class VendedorDeleteView(DeleteView):
    model = Vendedor
    template_name = 'vendedor_delete.html'
    success_url = reverse_lazy('vendedor_home')
    context_object_name = 'vendedor'