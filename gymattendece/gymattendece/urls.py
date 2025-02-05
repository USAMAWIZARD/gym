"""gymattendece URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gymattendeceapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mark/',views.markattendence),
    path('markuserattendence/',views.markuserattendence),
    path('allmember/',views.allmemberdisplayneartoexpier),
    path('newentries/',views.newentries),
    path('register/',views.register),
    path('expieredmembers/',views.expieredmembers),
    path('getalreadyexistdata/',views.getalreadyexistdata),
    path('registeruserdata/',views.registeruserdata),
    path('todaysattendence/',views.todaysattendence),
    path('getstatusofdate/<str:viewdateattendece>',views.getstatusofdate),
]
