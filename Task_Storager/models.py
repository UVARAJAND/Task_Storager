from django.db import models

# Create your models here.
class Tasks(models.Model):
    Time=models.TimeField(default="")
    Task_Name=models.CharField(max_length=200,default="")
