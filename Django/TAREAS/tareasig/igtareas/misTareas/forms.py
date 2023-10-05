from django import forms
from .models import Tareas

class tareasForm(forms.ModelForm):
	class Meta:
		model = Tareas
		fields = ('usuario','titulo','descripcion','complete')
		widgets = {
			'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
			'descripcion' : forms.Textarea(attrs={'class': 'form-control', 'rows':'3', 'cols':'5'})
		}
