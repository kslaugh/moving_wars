from django.shortcuts import render,redirect
from .models import Administrator,NewAdmin,Prospectors,ProVehicles
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
    if 'user' not in request.session:
        messages.error(request,"You must be logged in to do that!")
        return redirect('/admin/')
    context={
        'user':Administrator.objects.get(id=request.session['user']),
        'new_users':NewAdmin.objects.all(),
        'all_admin':Administrator.objects.all(),
        'pros':Prospectors.objects.all()
    }
    return render(request,'admin-home.html',context)

def actadmin(request, id):
    new=NewAdmin.objects.get(id=id)
    Administrator.objects.create(
        first_name=new.first_name,
        last_name=new.last_name,
        email=new.email,
        password=new.password,
        admin=Administrator.objects.get(id=request.session['user'])
    )
    new.delete()
    return redirect('/admin/home')

def denadmin(request, id):
    NewAdmin.objects.get(id=id).delete()
    return redirect('/admin/home')

def deladmin(request, id):
    Administrator.objects.get(id=id).delete()
    return redirect('/admin/home')

def logout(request):
    request.session.clear()
    return redirect('/admin/')

def delpro(request, id):
    pro=Prospectors.objects.get(id=id)
    pro.delete()
    return redirect('/admin/home')

def actpro(request, id):
    pass

def viewpro(request, id):
    pro=Prospectors.objects.get(id=id)
    context={
        'pro':pro,
        'v':pro.vehicles.first()
    }
    return render(request,'admin-pro.html',context)