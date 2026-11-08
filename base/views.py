from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Tarea

# Vista para logeate
class Login(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list-tareas')

# vista para crear un nuevo usuario
class Registro(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('list-tareas')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(Registro, self).form_valid(form)

     #compramos si hay un usuario logeado para controloar que no pueda ir a la ruta de registro
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list-tareas')
        return super(Registro, self).get(*args, **kwargs)


# vista para listar las tareas
class ListarTareas(LoginRequiredMixin, ListView):
    model = Tarea # selecciona hace referencia a la clase y obtiene todas las tareas
    context_object_name = 'tareas' # Cambia el nombre la variable con la que tenemos acceso a las tereas en la view

    #paso parametros a la vista donde le llega una variable con el nombre del al key
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()

        volar_busqueda = self.request.GET.get('buscador') or ''
        if volar_busqueda:
            context['tareas'] = context['tareas'].filter(titulo__icontains=volar_busqueda)
        context['volar_busqueda'] = volar_busqueda
        return context


# vista mostar los detalles de las tareas
class DetallesTareas(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/detalles_tareas.html' # Cambia el nombre default de la vista

# vista crear una nueva tarea
class CrearTareas(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo'] # hace un formulario con todas los campos de la clase
    success_url = reverse_lazy('list-tareas') # Redirige a la vista (por en name) si a salido todo bien

    # le ponemos el volor a el campo de usuario que es el usuario logeado
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTareas, self).form_valid(form)

# vista para editar una tarea
class EditarTareas(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('list-tareas')

# vista para la comfirmacion de elimiar la tarea
class EliminarTareas(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('list-tareas')
    template_name = 'base/eliminar_tarea.html'
