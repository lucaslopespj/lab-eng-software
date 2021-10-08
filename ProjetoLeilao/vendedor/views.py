from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Vendedor

class VendedorListView(ListView):
    model = Vendedor
    template_name = 'vendedor_home.html'

class VendedorDetailView(DetailView):
    model = Vendedor
    template_name = 'vendedor_detail.html'
    context_object_name = 'vendedor'

class VendedorCreateView(CreateView):
    model = Vendedor
    template_name = 'vendedor_new.html'
    fields = '__all__'

class VendedorUpdateView(UpdateView):
    model = Vendedor
    fields = ['bio'] #Only Editable Fields
    template_name = 'vendedor_edit.html'

class VendedorDeleteView(DeleteView):
    model = Vendedor
    template_name = 'vendedor_delete.html'
    success_url = reverse_lazy('vendedor_home')