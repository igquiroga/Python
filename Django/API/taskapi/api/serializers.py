from rest_framework import serializers
from .models import Tasks

class TasksAdminSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tasks
		fields = ['task_id','task_title','task_date','task_description','task_status','user_id']
class TasksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tasks
		fields = ['task_title','task_date','task_description','task_status']
class PostTasksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tasks
		fields = ['task_title','task_date','task_description','user_id']
class PutTasksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tasks
		fields = ['task_title','task_date','task_description','task_status']
class StatusTasksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tasks
		fields = ['task_id','task_status']