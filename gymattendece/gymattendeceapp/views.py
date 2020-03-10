from django.shortcuts import render
from Models import gym
# Create your views here.
def markattendence(request):
	return render(request,"markattendence.html")
def register(request):
	return render(request,"registeruser.html")
def registeruserdata(request):
	pass