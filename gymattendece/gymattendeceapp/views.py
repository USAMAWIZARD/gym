from django.shortcuts import render
from .models import gym

def markattendence(request):
	return render(request,"markattendence.html")
def register(request):
	return render(request,"registeruser.html")

def registeruserdata(request):
	gy=gym()
	name=request.POST["name"]
	gy.age=request.POST["age"]
	gy.phoneno=request.POST["number"]
	gy.joiningdate=request.POST["joiningdate"]
	gy.endingdate="32"
	gy.save()
	return render(request,"registeruser.html")