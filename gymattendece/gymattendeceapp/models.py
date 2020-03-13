from django.db import models

# Create your models here.
class gym(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phoneno = models.IntegerField()
    joiningdate = models.DateField(blank=True, null=True)
    endingdate = models.DateField(blank=True, null=True)
class admin(models.Model):
	adminname = models.CharField(max_length=255)
	adminpass = models.CharField(max_length=255)