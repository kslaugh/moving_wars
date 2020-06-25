from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from datetime import timedelta

from .models import *

# Create your views here.
def user(request):
    return render(request, "user.html")

def dashboard(request):
    if "customer_id" not in request.session:
        messages.error(request, "You must be logged in for that")
        return redirect('/')

    context={
        'customer':Customers.objects.get(id=request.session["customer_id"]),
        'jobs':reversed(Jobs.objects.all())
    }
    return render(request, "dashboard.html",context)

def create_user(request):
    errors = Customers.objects.basic_validator(request.POST)

    if len(errors)>0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')

    hashed_pw = bcrypt.hashpw(
        request.POST["password"].encode(),bcrypt.gensalt()
    ).decode() 
    created_user=Customers.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        phone=request.POST["phone"],
        email=request.POST["email"],
        password=hashed_pw,
    )

    request.session["customer_id"] = created_user.id
    
    return redirect('/dashboard')

def login(request):
    potential_users= Customers.objects.filter(email=request.POST['email'])

    if len(potential_users) == 0:
        messages.error(request, "Please check you email and Password")
        return redirect ('/')

    if bcrypt.checkpw(
        request.POST["password"].encode(),
        potential_users[0].password.encode(),
    ):
        request.session['customer_id'] = potential_users[0].id
        return redirect('/dashboard')

    messages.error(request, "Please check you email and Password")
    return redirect ('/')

def logout(request):
    request.session.clear()

    return redirect('/')

def new_job(request):

    context={
        'customer':Customers.objects.get(id=request.session['customer_id']),
        
    }
    return render(request, 'new_job.html', context)

def add_job(request):
    if 'fragile' in request.POST:
        frag=True
    else:
        frag=False

    Jobs.objects.create(
        title=request.POST["title"],
        start_location=request.POST["start_location"],
        end_location=request.POST["end_location"],
        description=request.POST["description"],
        attributes=request.POST["attributes"],
        fragile=frag,
        vehicle_type=request.POST["vehicle_type"],
        duration=timedelta(hours=int(request.POST['duration'])),
        customer=Customers.objects.get(id=request.session['customer_id']),
        date=request.POST["date"],
        time=request.POST["time"],

    )
    return redirect('/dashboard')