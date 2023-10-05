from .models import UsuariosTareas
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class loginForm (AuthenticationForm):
	class Meta:
		model = UsuariosTareas
		fields = ('nombreUsuario','claveUsuario')
		widgets = {
			'nombreUsuario' : forms.TextInput(attrs={'class': 'form-control'}),
			'claveUsuario' : forms.TextInput(attrs={'class': 'form-control'})
		}
