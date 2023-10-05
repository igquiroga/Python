from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import tareasForm
from misTareas.models import Tareas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
class TareasViewList(LoginRequiredMixin,ListView):
	model = Tareas
	context_object_name = 'misTareas'
	template_name = 'tareas.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['misTareas'] = context['misTareas'].filter(usuario=self.request.user)
		context['count'] = context['misTareas'].filter(complete=False).count()
		buscar_input = self.request.GET.get('tareaBuscar') or ""
		if buscar_input:
			context["misTareas"] = context["misTareas"].filter(
				titulo__icontains=buscar_input)
			#titulo__startswith
		context['buscar_input'] = buscar_input
		return context
class TareasViewDetalles(LoginRequiredMixin,DetailView):
	model = Tareas 
	context_object_name = 'misTareas'
	template_name = 'detalleTarea.html'
class TareasViewCrear(LoginRequiredMixin,CreateView):
	model = Tareas
	template_name = 'formTarea.html'
	form_class = tareasForm
	#fields = ['titulo','descripcion','complete']
	success_url = reverse_lazy('tareas')
	def get_context_data(self,*args, **kwargs):
		context = super(TareasViewCrear, self).get_context_data(*args,**kwargs)
		context['boton'] = 'Crear tarea'
		return context
	def form_valid(self,form):
		form.instance.usuario = self.request.user
		return super(TareasViewCrear, self).form_valid(form)


class TareasViewModificar(LoginRequiredMixin,UpdateView):
	model = Tareas
	template_name = 'formTarea.html'
	form_class = tareasForm
	#fields = ['titulo','descripcion','complete']
	success_url = reverse_lazy('tareas')
	def get_context_data(self,*args, **kwargs):
		context = super(TareasViewModificar, self).get_context_data(*args,**kwargs)
		context['boton'] = 'Modificar tarea'
		return context
	def form_valid(self,form):
		form.instance.usuario = self.request.user
		return super(TareasViewModificar, self).form_valid(form)
class TareasViewDelete(LoginRequiredMixin,DeleteView):
	model = Tareas
	template_name = 'eliminarTarea.html'
	context_object_name = 'misTareas'
	success_url = reverse_lazy('tareas')
	def form_valid(self,form):
		form.instance.usuario = self.request.user
		return super(TareasViewDelete, self).form_valid(form)
class TareasViewComplete(LoginRequiredMixin,UpdateView):
	model = Tareas
	template_name = 'completarTarea.html'
	form_class = tareasForm
	context_object_name = 'misTareas'
	success_url = reverse_lazy('tareas')
	def form_valid(self,form):
		form.instance.usuario = self.request.user
		form.instance.complete = 1
		return super(TareasViewComplete, self).form_valid(form)
class TareasViewPendiente(LoginRequiredMixin,UpdateView):
	model = Tareas
	template_name = 'pendienteTarea.html'
	form_class = tareasForm
	context_object_name = 'misTareas'
	success_url = reverse_lazy('tareas')
	def form_valid(self,form):
		form.instance.usuario = self.request.user
		form.instance.complete = 0
		return super(TareasViewPendiente, self).form_valid(form)

class TareasViewJson(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
	    return super(TareasViewJson, self).dispatch(request, *args, **kwargs)
	def get(self, request,id):
		if(id):
			listadoTareas = list(Tareas.objects.filter(id=id).values())
			if(len(listadoTareas) > 0):
				tarea = listadoTareas[0]
				datos = {'message':"Success",'tarea': listadoTareas}
			else:
				datos = {'message':"Tarea no encontrada"}
			return JsonResponse(datos)
class TareasViewPruebas(LoginRequiredMixin,ListView):
	model = Tareas
	context_object_name = 'misTareas'
	template_name = 'pruebas.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['misTareas'] = context['misTareas'].filter(usuario=self.request.user)
		context['count'] = context['misTareas'].filter(complete=False).count()
		buscar_input = self.request.GET.get('tareaBuscar') or ""
		if buscar_input:
			context["misTareas"] = context["misTareas"].filter(
				titulo__icontains=buscar_input)
			#titulo__startswith
		context['buscar_input'] = buscar_input
		return context