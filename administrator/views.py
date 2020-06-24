from django.shortcuts import render,redirect
from .models import Administrator,NewAdmin
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'admin.html')

def reg(request):
    return render(request,'admin-reg.html')

def register(request):
    e=Administrator.objects.regVals(request.POST)
    if len(e)==0:
        pw=bcrypt.hashpw(request.POST['p'].encode(),bcrypt.gensalt()).decode()
        NewAdmin.objects.create(
            first_name=request.POST['f'],
            last_name=request.POST['l'],
            email=request.POST['e'],
            password=pw
            )
        messages.error(request,"Registration-request sent")
        messages.error(request,"Please consult another Administrator for access")
        return redirect('/admin/')
    else:
        for i in e.values():
            messages.error(request,i)
        return redirect('/admin/reg')

def log(request):
    e=Administrator.objects.logVals(request.POST)
    if len(e)==0:
        request.session['user']=Administrator.objects.get(email=request.POST['e']).id
        return redirect('/admin/home')
    else:
        for i in e.values():
            messages.error(request,i)
        return redirect('/admin/')

def home(request):
    context={
        'user':Administrator.objects.get(id=request.session['user']),
        'new_users':NewAdmin.objects.all()
    }
    return render(request,'admin-home.html',context)

def actadmin(request):
    pass

def denadmin(request):
    pass