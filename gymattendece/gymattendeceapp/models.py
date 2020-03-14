from django.db import models
from gymattendece import settings 
# Create your models here.
class gym(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phoneno = models.CharField(max_length=11)
    joiningdate = models.DateField()
    endingdate = models.DateField()
class admin(models.Model):
	adminname = models.CharField(max_length=255)
	adminpass = models.CharField(max_length=255)
class attendence(models.Model):
	status=models.CharField(max_length=500)
	date=models.DateField()