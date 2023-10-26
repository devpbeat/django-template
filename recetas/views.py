from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Receta

# Create your views here.

class RecetaList(ListView):
    model = Receta
    template_name = 'recetas/list.html'
    context_object_name = 'recipes'
    
class RecetaDetalle(DetailView):
    model = Receta
    template_name = 'recetas/detail.html'
    context_object_name = 'recipe'
    
class RecetaCrear(CreateView):
    model = Receta
    template_name = 'recetas/create.html'
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('receta_lista')
    
class RecetaActualizar(UpdateView):
    model = Receta
    template_name = 'recetas/update.html'
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('receta_lista')
    
class RecetaEliminar(DeleteView):
    model = Receta
    template_name = 'recetas/delete.html'
    success_url = reverse_lazy('receta_lista')
    