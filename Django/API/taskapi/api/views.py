from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authtoken.models import Token
from .models import Tasks
from .serializers import *
from django.http import JsonResponse

class TasksApiView(APIView):
	permission_classes = (IsAuthenticated,) 
	def get(self,request,*args,**kwargs):
		my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
		user_id = Token.objects.get(key=my_token).user_id
		if user_id == 1:
			tasks = Tasks.objects.all()
		else:
			tasks = Tasks.objects.filter(user_id=user_id)
		if tasks:
			if user_id == 1:
				serializer = TasksAdminSerializer(tasks, many=True)
			else:
				serializer = TasksSerializer(tasks, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			response = {'Message':'No tasks found'}
			return Response(response,status = status.HTTP_200_OK)
	def post(self,request,*args,**kwargs):
		try:
			my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
			user_id = Token.objects.get(key=my_token).user_id
			data = {
				'task_title' : request.data.get('task_title'),
				'task_description' : request.data.get('task_description'),
				'task_date' : request.data.get('task_date'),
				'user_id' : user_id
			}
			serializer = PostTasksSerializer(data=data)
			if serializer.is_valid():
				serializer.save()
				response = {'Message':'Task Created'}
				return Response(response,status=status.HTTP_201_CREATED)
			else:
				return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			response = {'Message':'BAD_REQUEST','Error': f'{e}'}
			return Response(response,status=status.HTTP_400_BAD_REQUEST)
	def put(self,request,*args,**kwargs):
		try:
			task_id = request.data.get('task_id')
			task = Tasks.objects.get(task_id=task_id)
			if task:
				data = {
					'task_title' : request.data.get('task_title'),
					'task_description' : request.data.get('task_description'),
					'task_date' : request.data.get('task_date'),
					'task_status' : request.data.get('task_status')
				}
				serializer = PutTasksSerializer(task,data=data)
				if serializer.is_valid():
					serializer.save()
					response = {'Message':'Task updated'}
					return Response(response,status=status.HTTP_201_CREATED)
				else:
					return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			response = {'Message':f'{e}'}
			return Response(response,status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request,*args,**kwargs):
		try:
			task_id = request.data.get('task_id')
			task = Tasks.objects.get(task_id=task_id)
			if task:
				task.delete()
				msj = f'Task {task_id} deleted'
				response = {'Message': msj}
				return Response(response,status=status.HTTP_200_OK)
		except Exception as e:
			response = {'Message':f'{e}'}
			return Response(response,status=status.HTTP_400_BAD_REQUEST)
class TasksApiViewId(APIView):
	permission_classes = (IsAuthenticated,) 
	def get(self,request,*args,**kwargs):
		try:
			task_id = kwargs['task_id']
			task = Tasks.objects.filter(task_id=task_id)
			if task:
				serializer = TasksSerializer(task, many=True)
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				response = {'Message':'Task not found'}
				return Response(response,status=status.HTTP_404_NOT_FOUND)
		except:
			response = {'Message':'BAD_REQUEST'}
			return Response(response,status=status.HTTP_400_BAD_REQUEST)
class TaskApiChangeStatus(APIView):
	permission_classes = (IsAuthenticated,) 
	def put(self,request,*args,**kwargs):
		try:
			task_id = request.data.get('task_id')
			task = Tasks.objects.get(task_id=task_id)
			if task:
				data = {
					'task_id' : request.data.get('task_id'),
					'task_status' : request.data.get('task_status')
				}
				serializer = StatusTasksSerializer(task,data=data)
				if serializer.is_valid():
					serializer.save()
					response = {'Message':'Task updated'}
					return Response(response,status=status.HTTP_201_CREATED)
				else:
					return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			response = {'Message':f'{e}'}
			return Response(response,status=status.HTTP_400_BAD_REQUEST)