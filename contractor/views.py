from django.shortcuts import render, redirect
from .models import Contractors,Vehicles,Ratings,Reviews,Bids
from administrator.models import Prospectors,ProVehicles
from user.models import Jobs
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'contractor.html')

def log(request):
    e=Contractors.objects.logVals(request.POST)
    if len(e)==0:
        request.session['cont']=Contractors.objects.get(email=request.POST['e']).id
        return redirect('/contractor/home')
    else:
        for i in e.values():
            messages.error(request,i)
        return redirect('/contractor/')

def reg(request):
    return render(request,'cont-reg.html')

def register(request):
    e={**Contractors.objects.regVals(request.POST),**Vehicles.objects.veVals(request.POST)}
    if len(e)==0:
        pw=bcrypt.hashpw(request.POST['p'].encode(),bcrypt.gensalt()).decode()
        Prospectors.objects.create(
            fname=request.POST['f'],
            lname=request.POST['l'],
            email=request.POST['e'],
            phone=request.POST['ph1']+request.POST['ph2']+request.POST['ph3'],
            password=pw
            )
        ProVehicles.objects.create(
            year=request.POST['y'],
            make=request.POST['ma'],
            model=request.POST['mo'],
            vehicle_type=request.POST['vt'],
            owner=Prospectors.objects.last()
        )
        messages.success(request,"Contractor Application sent")
        messages.success(request,"Your account will be approved within a couple days")
        return redirect('/contractor/')
    else:
        for i in e.values():
            messages.error(request,i)
        return redirect('/contractor/reg')

def home(request):
    c=Contractors.objects.get(id=request.session['cont'])
    all_vehicles=c.vehicles.all()
    vts={}
    avail_jobs=[]
    for i in all_vehicles:
        vts[i.vehicle_type]= +1
    vts2=[]
    for x in vts:
        vts2.append(x)
    for j in vts2:
        print(j)
        if len(avail_jobs)<1:
            avail_jobs=Jobs.objects.filter(vehicle_type=j)
        avail_jobs|=Jobs.objects.filter(vehicle_type=j)
    print(avail_jobs)
    context={
        'user':Contractors.objects.get(id=request.session['cont']),
        'jobs':avail_jobs
    }
    return render(request,'cont-home.html',context)

def addv(request):
    context={
        'user':Contractors.objects.get(id=request.session['cont'])
    }
    return render(request,'cont-vehicle.html',context)

def addvehicle(request):
    Vehicles.objects.create(
        year=request.POST['y'],
        make=request.POST['ma'],
        model=request.POST['mo'],
        vehicle_type=request.POST['vt'],
        owner=Contractors.objects.get(id=request.session['cont'])
    )
    return redirect('/contractor/home')

def logout(request):
    request.session.clear()
    return redirect('/contractor/')

def viewjob(request,id):
    context={
        'user':Contractors.objects.get(id=request.session['cont']),
        'job':Jobs.objects.get(id=id)
    }
    return render(request,"cont-job.html",context)

def cancel (request):
    return redirect('/contractor/home')

def bid(request,id):
    context={
        'user':Contractors.objects.get(id=request.session['cont']),
        'job':Jobs.objects.get(id=id)
    }
    return render(request,"cont-bid.html",context)

def placebid(request,id):
    if request.POST['a']=='':
        messages.error(request,'You must input an Amount')
        return redirect('/contractor/'+str(id)+'/bid')
    Bids.objects.create(
        amount=request.POST['a'],
        jobs=Jobs.objects.get(id=id),
        contractor=Contractors.objects.get(id=request.session['cont'])
    )
    return redirect('/contractor/home')