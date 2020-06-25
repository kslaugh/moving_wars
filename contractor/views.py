from django.shortcuts import render, redirect
from .models import Contractors,Vehicles,Ratings,Reviews,Bids
from administrator.models import Prospectors,ProVehicles
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'contractor.html')

def log(request):
    e=Contractors.objects.logVals(request.POST)
    if len(e)==0:
        request.session['user']=Contractors.objects.get(email=request.POST['e']).id
        return redirect('/contractor/home')
    else:
        for i in e.values():
            messages.error(request,i)
        return redirect('/contractor/')

def reg(request):
    return render(request,'cont-reg.html')

def register(request):
    e=Contractors.objects.regVals(request.POST)
    if len(e)==0:
        pw=bcrypt.hashpw(request.POST['p'].encode(),bcrypt.gensalt()).decode()
        Prospectors.objects.create(
            first_name=request.POST['f'],
            last_name=request.POST['l'],
            email=request.POST['e'],
            phone=request.POST['ph1']+request.POST['ph2']+request.POST['ph3'],
            password=pw
            )
        messages.error(request,"Contractor Application sent")
        messages.error(request,"Your account will be approved within a couple days")
        return redirect('/admin/')
    else:
        for i in e.values():
            messages.error(request,i)
        return redirect('/admin/reg')