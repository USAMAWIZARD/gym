from django.shortcuts import render
from .models import gym
import datetime 
import calendar
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
	print(request.POST["joiningdate"])
	try:
		date_1 = datetime.datetime.strptime(request.POST["joiningdate"], "%m/%d/%Y").date()
	except:
		date_1 = datetime.datetime.strptime(request.POST["joiningdate"], "%Y-%m-%d").date()
	days_in_month = calendar.monthrange(date_1.year, date_1	.month)[1]
	end=datetime.datetime.strptime(str(date_1 +datetime.timedelta(days=days_in_month)), '%Y-%m-%d').strftime('%m/%d/%Y')

	gy.endingdate=end
	gy.save()
	return render(request,"registeruser.html")