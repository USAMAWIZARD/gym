from django.shortcuts import render,redirect
from .models import gym,attendence
import datetime 
from django.db import connection, transaction	
import calendar
from django.forms.models import model_to_dict
from django.db.models import Q
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
def markattendence(request):
	return render(request,"markattendence.html")
def register(request):
	return render(request,"registeruser.html")

def registeruserdata(request):
	if request.POST["membertype"]=="old":

		gy=gym.objects.get(id=request.POST["idofalreadyexistmem"])
	else:
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



def markuserattendence(request):
	try:
		gym.objects.get(id=request.POST["gymid"]) #if user exist
	except:
		return redirect("/mark/")
	#ifuserexist=attendence.objects.filter(date=).count()
	ifdateexist=attendence.objects.filter(date=datetime.date.today().strftime("%Y-%m-%d")).count()
	todaydate=datetime.date.today().strftime("%Y-%m-%d")
	a=attendence()
	try:
		i=attendence.objects.get(date=todaydate)
	except:
		a.date=str(datetime.date.today().strftime("%Y-%m-%d"))
		a.status=request.POST["gymid"]	
		a.save()
		return redirect('/mark/')
	i.status=i.status+','+request.POST["gymid"]
	i.save()
	return redirect("/mark/")
	 
def allmemberdisplayneartoexpier(request):
	return render(request,'adminalluser.html',{'gymuser':gym.objects.values_list().order_by('endingdate')})

def newentries(request):
	return render(request,'adminalluser.html',{'gymuser':gym.objects.values_list().order_by('-endingdate')})

def expieredmembers(request):
	today=str(datetime.date.today().strftime("%Y-%m-%d"))
	return render(request,'adminalluser.html',{'gymuser':gym.objects.filter(endingdate__lte=today).values_list()})

def getalreadyexistdata(request):
	dictt={}

	member=gym.objects.get(id= request.POST['memid']);
	dictt["name"]=member.name
	dictt["age"]=member.age
	dictt["phoneno"]=member.phoneno
	dictt["startindate"]=member.joiningdate
	dictt["endingdate"]=member.endingdate

	return  JsonResponse({'dictt': dictt})
