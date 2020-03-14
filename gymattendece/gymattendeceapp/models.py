from django.db import models

# Create your models here.
class gym(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phoneno = models.CharField(max_length=11)
    joiningdate = models.CharField(max_length=255)
    endingdate = models.CharField(max_length=255)
class admin(models.Model):
	adminname = models.CharField(max_length=255)
	adminpass = models.CharField(max_length=255)