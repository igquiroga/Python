from django.db import models
class Tasks(models.Model):
	task_id = models.AutoField(primary_key=True,verbose_name='taks_id')
	user_id = models.IntegerField(null=True,verbose_name='user_id')
	task_title = models.CharField(max_length=255,verbose_name='task_title')
	task_date = models.DateField(verbose_name='task_date')
	task_description = models.TextField(max_length=255,verbose_name='task_description')
	task_status = models.BooleanField(default=False)
