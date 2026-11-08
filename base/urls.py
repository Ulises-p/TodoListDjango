from django.urls import path
from .views import ListarTareas, DetallesTareas, CrearTareas, EditarTareas, EliminarTareas, Login, Registro
from django.contrib.auth.views import LogoutView

urlpatterns = [path('', ListarTareas.as_view(), name='list-tareas'),
               path('login/', Login.as_view(), name='login'),
               path('register/', Registro.as_view(), name='register'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('tarea/<int:pk>', DetallesTareas.as_view(), name='tarea'),
               path('crearTarea/', CrearTareas.as_view(), name='crear-tarea'),
               path('editarTarea/<int:pk>', EditarTareas.as_view(), name='editar-tarea'),
               path('eliminarTareas/<int:pk>', EliminarTareas.as_view(), name='eliminar-tarea'),
               ]