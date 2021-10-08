from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Leiloeiro

class LeiloeiroListView(ListView):
    model = Leiloeiro
    template_name = 'leiloeiro_home.html'

class LeiloeiroDetailView(DetailView):
    model = Leiloeiro
    template_name = 'leiloeiro_detail.html'
    context_object_name = 'leiloeiro'

class LeiloeiroCreateView(CreateView):
    model = Leiloeiro
    template_name = 'leiloeiro_new.html'
    fields = '__all__'

class LeiloeiroUpdateView(UpdateView):
    model = Leiloeiro
    fields = ['bio'] #Only Editable Fields
    template_name = 'leiloeiro_edit.html'

class LeiloeiroDeleteView(DeleteView):
    model = Leiloeiro
    template_name = 'leiloeiro_delete.html'
    success_url = reverse_lazy('leiloeiro_home')