from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.template import loader
import requests
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework.authtoken.models import Token

"""
def home(request):
    plantilla = loader.get_template('home.html')
    context = {
        'title': 'TASK API',
    }
    return HttpResponse(plantilla.render(context,request))
def viewTasks(request): 
    if request.method == "POST":
        if request.POST["changeStatus"] == "0":
            status = True
        if request.POST["changeStatus"] == "1":
            status = False
        data = {
            'task_id' : request.POST["task_id"],
            'task_status' : status
        }
        changeRequest = requests.put("http://localhost:8000/api/changeStatus/",data=data)  
    plantilla = loader.get_template('tasks.html')
    url = "http://localhost:8000/api/"
    headers = {'Authorization': 'Token 71eabfcc222da2ae6fcaa20005d84924f9c50af8'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        data = response.json() 
    else:
        data = {'Error':'No tasks found'}
    context = {
        'title': 'TASK API',
        'data' : data,
    }
    return HttpResponse(plantilla.render(context,request))

def addTask(request):
    if request.method == "POST":
        data = {
        'task_title' : request.POST["task_title"],
        'task_date' : request.POST["task_date"],
        'task_description' : request.POST["task_description"],
        }
        url = "http://localhost:8000/api/"
        response = requests.post(url,data=data)
        if response.status_code == 201:
            url = reverse('view-tasks')
        if response.status_code == 400:
            url = reverse('add-task')
        return HttpResponseRedirect(url)
    if request.method == "GET":
        plantilla = loader.get_template('addtask.html')
        context = {
            'title': 'TASK API',
        }
        return HttpResponse(plantilla.render(context,request))

def modifyTask(request,task_id):
    if request.method == "POST":
        data = {
        'task_id' : request.POST["task_id"],
        'task_title' : request.POST["task_title"],
        'task_date' : request.POST["task_date"],
        'task_description' : request.POST["task_description"],
        'task_status' : request.POST["task_status"],
        }
        response = requests.put("http://localhost:8000/api/",data=data)
        if response.status_code == 201:
            url = reverse('view-tasks')
        if response.status_code == 404:
            url = reverse('modify-task',kwargs={'task_id':task_id})
        if response.status_code == 400:
            url = reverse('modify-task',kwargs={'task_id':task_id})
        return HttpResponseRedirect(url)
    if request.method == "GET":
        plantilla = loader.get_template('modifytask.html')
        current_user = request.user
        my_token = Token.objects.get(user_id=current_user.id)
        headers = {'Authorization': f'Token {my_token}'}
        url = f'http://localhost:8000/api/{task_id}'
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            data = response.json()
        if response.status_code == 404:
             return HttpResponseRedirect(reverse('view-tasks'))
        context = {
            'title': 'TASK API',
            'data' : data
        }
        return HttpResponse(plantilla.render(context,request))

    
def deleteTask(request,task_id):
    if request.method == "POST":
        data = {
        'task_id' : request.POST["task_id"]
        }
        response = requests.delete("http://localhost:8000/api/",data=data)
        return HttpResponseRedirect(reverse('view-tasks'))
    if request.method == "GET":
        plantilla = loader.get_template('deletetask.html')
        response = requests.get(f'http://localhost:8000/api/{task_id}')
        context = {
            'title': 'TASK API',
            'task_id' : task_id
        }
        if response.status_code == 404:
            return HttpResponseRedirect(reverse('view-tasks'))
        if response.status_code == 400:
            return HttpResponseRedirect(reverse('view-tasks'))
        return HttpResponse(plantilla.render(context,request)) 
"""   
class TasksViewLoginUser(LoginView):
    template_name = "login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('user-info')
    def form_invalid(self, form):
        print(form.errors)
        return super(tareasViewLogin, self).form_invalid(form)
class TasksViewCreateUser(FormView):
    template_name = "createuser.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('user-info')
    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(TasksViewCreateUser,self).form_valid(form)
    def form_invalid(self, form):
        print(form.errors)
        return super(TasksViewCreateUser, self).form_invalid(form)
class TasksViewMyAccount(LoginRequiredMixin,TemplateView):
    template_name = "myaccount.html"
    login_url = 'user-login'
class TasksViewInfoUser(LoginRequiredMixin,TemplateView):
    template_name = "accountinfo.html"
    login_url = 'user-login' 
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'TASK API'
        context['istoken'] = kwargs["istoken"]
        context['my_token'] = kwargs["token"]
        return context
    def get(self, request, *args, **kwargs):
        current_user = request.user
        try:
            my_token = Token.objects.get(user_id=current_user.id)
            context = self.get_context_data(istoken=True,token= my_token)
        except Exception as e:
            context = self.get_context_data(istoken=False,token="No token avalaible")
        return self.render_to_response(context)
    def post(self,request, *args,**kwargs):
        current_user = request.user
        token = Token.objects.create(user=current_user)
        return HttpResponseRedirect(reverse('user-info'))
class TasksViewList(LoginRequiredMixin,TemplateView):
    template_name = 'mytasks.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'TASK API'
        context['data'] = kwargs["data"]
        context['isdata'] = kwargs["isdata"]
        return context
    def get(self, request, *args, **kwargs):
        url = "http://localhost:8000/api/"
        current_user = request.user
        try:
            my_token = Token.objects.get(user_id=current_user.id)
            headers = {'Authorization': f'Token {my_token}'}
            response = requests.get(url,headers=headers)
            if response.status_code == 200:
                data = response.json() 
                context = self.get_context_data(isdata=True,data=data)
            else:
                data = {'error':'No tasks found'}
                context = self.get_context_data(isdata=False,data=data)
            return self.render_to_response(context)
        except:
            data = {'error' : 'No token avalaible'}
            context = self.get_context_data(isdata=False,data=data)
            return self.render_to_response(context)
    def post(self,request, *args,**kwargs):
        postStatus = request.POST['changeStatus'] if 'changeStatus' in request.POST else None
        if(postStatus):
            if request.POST["changeStatus"] == "0":
                status = True
            if request.POST["changeStatus"] == "1":
                status = False
            data = {
                'task_id' : request.POST["task_id"],
                'task_status' : status
            }
            current_user = request.user
            my_token = Token.objects.get(user_id=current_user.id)
            headers = {'Authorization': f'Token {my_token}'}
            changeRequest = requests.put("http://localhost:8000/api/changeStatus/",headers=headers,data=data)
        postDelete = request.POST['task_id_delete'] if 'task_id_delete' in request.POST else None
        if(postDelete): 
            data = {
            'task_id' : request.POST["task_id_delete"]
            }
            current_user = request.user
            my_token = Token.objects.get(user_id=current_user.id)
            headers = {'Authorization': f'Token {my_token}'}
            url = "http://localhost:8000/api/"
            response = requests.delete(url,headers=headers,data=data)
        return HttpResponseRedirect(reverse('my-tasks'))

class AddTaskViewList(LoginRequiredMixin,TemplateView):
    template_name = 'addtask.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'TASK API'
        context['istoken'] = kwargs["istoken"]
        return context
    def get(self,request,*args,**kwargs):
        current_user = request.user
        try:
            my_token = Token.objects.get(user_id=current_user.id)
            context = self.get_context_data(istoken=True)
        except:
            context = self.get_context_data(istoken=False)
        return self.render_to_response(context)
    def post(self,request,*args,**kwargs):
        current_user = request.user
        my_token = Token.objects.get(user_id=current_user.id)
        headers = {'Authorization': f'Token {my_token}'}
        data = {
        'task_title' : request.POST["task_title"],
        'task_date' : request.POST["task_date"],
        'task_description' : request.POST["task_description"],
        }
        urlapi = "http://localhost:8000/api/"
        response = requests.post(urlapi,data=data,headers=headers)
        if response.status_code == 201:
            url = reverse('my-tasks')
        elif response.status_code == 400:
            url = reverse('add-task')
        return HttpResponseRedirect(url)
class modifyTaskView(LoginRequiredMixin,TemplateView):
    template_name = 'modifytask.html'
    def get(self,request,*args,**kwargs):
        task_id = kwargs["task_id"]
        current_user = request.user
        my_token = Token.objects.get(user_id=current_user.id)
        headers = {'Authorization': f'Token {my_token}'}
        url = f'http://localhost:8000/api/{task_id}'
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            data = response.json()
        if response.status_code == 404:
             return HttpResponseRedirect(reverse('my-task'))
        context = self.get_context_data(data=data)
        return self.render_to_response(context)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'TASK API'
        context['data'] = kwargs["data"]
        return context
    def post(self,request,*args,**kwargs):
        data = {
        'task_id' : request.POST["task_id"],
        'task_title' : request.POST["task_title"],
        'task_date' : request.POST["task_date"],
        'task_description' : request.POST["task_description"],
        'task_status' : request.POST["task_status"],
        }
        current_user = request.user
        my_token = Token.objects.get(user_id=current_user.id)
        headers = {'Authorization': f'Token {my_token}'}
        response = requests.put("http://localhost:8000/api/",data=data,headers=headers)
        if response.status_code == 201:
            url = reverse('my-tasks')
        if response.status_code == 404:
            url = reverse('modify-task',kwargs={'task_id':task_id})
        if response.status_code == 400:
            url = reverse('modify-task',kwargs={'task_id':task_id})
        return HttpResponseRedirect(url)
class deleteTaskView(LoginRequiredMixin,TemplateView):
    template_name = "deletetask.html"
    def post(self,request,*args,**kwargs):
        data = {
        'task_id' : request.POST["task_id"]
        }
        current_user = request.user
        my_token = Token.objects.get(user_id=current_user.id)
        headers = {'Authorization': f'Token {my_token}'}
        url = "http://localhost:8000/api/"
        response = requests.delete(url,headers=headers,data=data)
        return HttpResponseRedirect(reverse('my-tasks'))
    def get(self,request,*args,**kwargs):
        task_id = kwargs["task_id"]
        current_user = request.user
        my_token = Token.objects.get(user_id=current_user.id)
        headers = {'Authorization': f'Token {my_token}'}
        url = f'http://localhost:8000/api/{task_id}'
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            data = response.json()
        if response.status_code == 404:
            return HttpResponseRedirect(reverse('my-tasks'))
        if response.status_code == 400:
            return HttpResponseRedirect(reverse('my-tasks'))
        context = self.get_context_data(data=data,task_id=task_id)
        return self.render_to_response(context)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'TASK API'
        context['data'] = kwargs["data"]
        context['task_id'] = kwargs["task_id"]
        return context