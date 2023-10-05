from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Usuarios
from django.urls import reverse
def home(request):
    plantilla = loader.get_template('home.html')
    context = {
        'title': 'HOME',
    }
    return HttpResponse(plantilla.render(context,request))
def listado(request):
    plantilla = loader.get_template('listado.html')
    misUsuarios = Usuarios.objects.all().values()
    context = {
        'title': 'LISTADO',
        'usuarios' : misUsuarios
    }
    
    return HttpResponse(plantilla.render(context,request))
def crearUsuario(request):
    plantilla = loader.get_template('crearUsuario.html')
    context = {
        'title': 'CREAR USUARIO',
    }
    if request.method == "POST":
        nombreUsuario = request.POST['nombre']
        claveUsuario = request.POST['clave']
        nuevoUsuario = Usuarios(nombre=nombreUsuario,clave = claveUsuario)
        nuevoUsuario.save()
        return HttpResponseRedirect(reverse('listado'))
    return HttpResponse(plantilla.render(context,request))

def modificarUsuario(request,id):
    plantilla = loader.get_template('modificarUsuario.html')


    if request.method == "POST":
        idUsuario = request.POST['id']
        nombreUsuario = request.POST['nombre']
        claveUsuario = request.POST['clave']
        usuario = Usuarios.objects.get(id=idUsuario)
        usuario.nombre = nombreUsuario
        usuario.clave = claveUsuario
        usuario.save()
        return HttpResponseRedirect(reverse('listado'))
    else:
        idUsuario = id
        usuario = Usuarios.objects.get(id=idUsuario)
        context = {
            'title': 'MODIFICAR USUARIO',
            'usuario' : usuario  
        }
        return HttpResponse(plantilla.render(context,request))
    
def eliminarUsuario(request,id):
    plantilla = loader.get_template('eliminarUsuario.html')
    if request.method == "POST":
        idUsuario = request.POST['id']
        usuario = Usuarios.objects.get(id=idUsuario)
        usuario.delete()
        return HttpResponseRedirect(reverse('listado'))
    else:
        idUsuario = id
        usuario = Usuarios.objects.get(id=idUsuario)
        context = {
            'title': 'MODIFICAR USUARIO',
            'usuario': usuario
        }
        return HttpResponse(plantilla.render(context,request))
