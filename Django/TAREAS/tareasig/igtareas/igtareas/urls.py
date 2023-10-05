from django.contrib import admin
from django.urls import path
from userLogin.views import *
from misTareas.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tareasViewHome.as_view(), name='index'),
    path('acerca/', tareasViewAcerca.as_view(), name='acerca'),
    path('login', tareasViewLogin.as_view(), name='login'),
    path('registro/', tareasViewRegistro.as_view(), name='registro'),
    path('cerrarSesion', LogoutView.as_view(next_page='index'), name='logout'),
    path('tareas/', TareasViewList.as_view(), name='tareas'),
    path('crearTarea/', TareasViewCrear.as_view(), name='crearTarea'),
    path('detalleTarea/<int:pk>/', TareasViewDetalles.as_view(), name='detalleTarea'),
    path('modificarTarea/<int:pk>/', TareasViewModificar.as_view(), name='modificarTarea'),
    path('eliminarTarea/<int:pk>/', TareasViewDelete.as_view(), name='eliminarTarea'),
    path('completarTarea/<int:pk>/', TareasViewComplete.as_view(), name='completarTarea'),
    path('pendienteTarea/<int:pk>/', TareasViewPendiente.as_view(), name='pendienteTarea'),
    path('tareaig/<int:id>/',TareasViewJson.as_view(), name='tareaig'),
    path('pruebas/', TareasViewPruebas.as_view(), name='pruebas'),
]
