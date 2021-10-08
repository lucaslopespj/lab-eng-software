from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Comprador

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

class CompradorUpdateView(UpdateView):
    model = Comprador
    fields = ['bio'] #Only Editable Fields
    template_name = 'comprador_edit.html'

class CompradorDeleteView(DeleteView):
    model = Comprador
    template_name = 'comprador_delete.html'
    success_url = reverse_lazy('comprador_home')