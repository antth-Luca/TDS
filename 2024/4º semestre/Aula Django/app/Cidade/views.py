from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Cidade

# Create your views here.
class CreateCidadeView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('Entrada')
    model = Cidade
    fields = '__all__'
    template_name = 'Cidade/create-cidade.html'
    success_url = reverse_lazy('Home')


class ListCidadeView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('Entrada')
    model = Cidade
    template_name = 'Cidade/list-cidade.html'
    context_object_name = 'cidades'


class EditCidadeView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('Entrada')
    model = Cidade
    fields = '__all__'
    template_name = 'Cidade/edit-cidade.html'
    success_url = reverse_lazy('ListCidade')