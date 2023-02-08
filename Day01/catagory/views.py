from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from .models import *


# Create your views here.
#vire method(httprequest)--->return HttpResponse

def TempIndex(r):

    return render(r,'index.html')

def Test(r):
    return HttpResponse('Test')

def TempSite1(r):
    return render(r,'PriSection.html')

def TempAdd(r):
    return render(r,'AddSection.html')


def TempData(r):
    return HttpResponse(r,'data.py')

def Add(r):
    if(r.method =='GET'):
        return render(r,'AddSection.html')
    else:
        data=r.POST
        Sections.objects.create(section_name=data['FarmName'])
        Message={}
        Message['Alert']='Data ',data['FarmName'], ' Inserted'
    return render(r,'AddSection.html',Message)

def List(r):
    Message={}
    Message['ListSec']=Sections.objects.all()
    for msg in Message['ListSec']:
        print(msg.section_name)
    return render(r, 'ListSection.html',Message)

def UpdateSection(r,SID):
    if(r.method=='GET'):
        Upd=Sections.objects.get(id=SID)
        Message = {}
        Message['Upd'] = Upd
        return render(r, 'UpdateSection.html',Message)
    else:
        newUpd=r.POST
        Upd = Sections.objects.filter(id=SID).update(section_name=newUpd['FarmName'])
        Message = {}
        Message['ListSec'] = Sections.objects.all()
        return render(r, 'UpdateSection.html',Message)

def DeleteSection(r,DiD):
        Sections.objects.filter(id=DiD).delete()
        return HttpResponseRedirect('ListSections')

def AddData(r):
    BookS={}
    if(r.method=='GET'):
        BookS['ListSec']=Sections.objects.all()
        return render(r,'AddBook.html',BookS)
    else:
        Book.objects.create(bname=r.POST['BookName'],author=r.POST['BookAuth'],section=Sections.objects.get(id=r.POST['BookSection']))
        return render(r,'AddBook.html',BookS)



def logins(r):
        if (r.method == 'POST'):
            usr=AddUser.objects.filter(
                username=r.POST['username'],
                password=r.POST['password'],
            )
            ausr=authenticate(
                username=r.POST['username'],
                password=r.POST['password']
            )
            if (usr[0] is not None and ausr is not None):
                r.session['uid'] = usr[0].uid
                r.session['username'] = usr[0].username
                login(r,ausr)
                return HttpResponseRedirect('ListSections')
            else:
                Message={}
                Message['Alert']='username or password wrong'
                return render(r,'login.html',Message)
        else:
            return render(r,'login.html')

#@require_http_methods(['POST'])
def logout(r):
    r.session.clear()
    return HttpResponseRedirect('login')
def register(r):
    if(r.method=='POST'):
        AddUser.objects.create(
            username=r.POST['username'],
            password=r.POST['password'],
            email=r.POST['email']
        )
        User.objects.create_superuser(
            username=r.POST['username'],
            password=r.POST['password'],
            email=r.POST['email']
        )
        # r.session['uid']=x.uid
        # r.session['username']=x.username
        return render(r,'ListSection.html')
    else:
        return render(r, 'register.html')

class LoginView(View):
    def get(self,r):
        return render(r,'login.html')
    def post(self,r):
        return HttpResponse('Class view Post method')

class ListUsers(ListView):
    model = AddUser
