from .models import TasksUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class loginForm (AuthenticationForm):
	class Meta:
		model = UsuariosTareas
		fields = ('user_name','user_password')
		widgets = {
			'user_name' : forms.TextInput(attrs={'class': 'form-control'}),
			'user_password' : forms.TextInput(attrs={'class': 'form-control'})
		}
