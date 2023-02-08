"""Day01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from catagory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.TempIndex, name='DefaultTemp'),

    path('tst', views.Test, name='Test'),
    path('section', views.TempSite1, name='PriSection'),
    path('AddSections', views.Add, name='AddSection'),
    path('ListSections', views.List, name='ListSection'),
    path('AddDatas', views.AddData, name='insertData'),
    path('UpdateSections/<int:SID>', views.UpdateSection, name='UpdateSec'),
    path('DDDelete/<int:DiD>',views.DeleteSection,name='DeleteSection'),
    #path('login',views.logins,name='login'),
    path('login',views.LoginView.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('auser',views.ListUsers.as_view(),name='auser'),
]

