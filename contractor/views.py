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
        return redirect('/admin/home')
    else:
        for i in e.values():
            messages.error(request,i)
        return redirect('/admin/')

def reg(request):
    return render(request,'cont-reg.html')