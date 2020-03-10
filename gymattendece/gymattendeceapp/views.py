from django.shortcuts import render

# Create your views here.
def markattendence(request):
	return render(request,"markattendence.html")
def register(request):
	return render(request,"registeruser.html")