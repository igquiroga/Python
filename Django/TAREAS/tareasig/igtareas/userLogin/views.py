from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django import forms
from .forms import loginForm
from .models import UsuariosTareas
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class tareasViewHome(TemplateView):
	template_name = "home.html"
class tareasViewAcerca(TemplateView):
	template_name = "acerca.html"
class tareasViewLogin(LoginView):
	template_name = "login.html"
	fields = '__all__'
	redirect_authenticated_user = True
	def get_success_url(self):
		return reverse_lazy('tareas')
	def form_invalid(self, form):
		print(form.errors)
		return super(tareasViewLogin, self).form_invalid(form)
class tareasViewRegistro(FormView):
	template_name = "registro.html"
	form_class = UserCreationForm
	#redirect_authenticated_user = True
	success_url = reverse_lazy('tareas')
	def form_valid(self,form):
		usuario = form.save()
		if usuario is not None:
			login(self.request,usuario)
		return super(tareasViewRegistro,self).form_valid(form)
	def form_invalid(self, form):
		print(form.errors)
		return super(tareasViewRegistro, self).form_invalid(form)
	def get(self, *args , **kwargs):
		if self.request.user.is_authenticated:
			return redirect('tareas')
		return super(tareasViewRegistro,self).get(*args,**kwargs)