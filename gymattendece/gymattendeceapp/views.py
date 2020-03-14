from django.shortcuts import render,redirect
from .models import gym,attendence
import datetime 
import calendar
def markattendence(request):
	return render(request,"markattendence.html")
def register(request):
	return render(request,"registeruser.html")

def registeruserdata(request):
	gy=gym()
	gy.name=request.POST["name"]
	gy.age=request.POST["age"]
	gy.phoneno=request.POST["number"]
	
	#datetimeobject.strftime('%m-%d-%Y')
	print(request.POST["joiningdate"])
	try:
		date_1 = datetime.datetime.strptime(request.POST["joiningdate"], "%m-%d-%Y").date()
	except:
		date_1 = datetime.datetime.strptime(request.POST["joiningdate"], "%Y-%m-%d").date()
	gy.joiningdate=date_1.strftime('%Y-%m-%d')
	days_in_month = calendar.monthrange(date_1.year, date_1.month)[1]
	end=datetime.datetime.strptime(str(date_1 +datetime.timedelta(days=days_in_month)), '%Y-%m-%d').strftime('%Y-%m-%d')

	gy.endingdate=end
	gy.save()
	return render(request,"registeruser.html")
def adddateindb(request):
	a=attendence()
	b=attendence.objects.raw("select date from a where date="+datetime.date.today().strftime("%Y-%m-%d"))
	if attendence.objects.all().count()<1:
		a.date=str=datetime.date.today().strftime("%Y-%m-%d")
		a.save()
	return redirect("/mark/")