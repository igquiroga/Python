from django.db import models

class TasksUser(models.Model):
    user_id = models.AutoField(primary_key=True,verbose_name="user_id")
    user_name = models.CharField(max_length=255,verbose_name="user_name")
    user_password = models.CharField(max_length=255,verbose_name="user_password")
    def __str__(self):
        row = "id: " +str(self.user_id)+ ",Name:" + self.user_name
        return row
    empAuth_objects = models.Manager()