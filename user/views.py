from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from datetime import timedelta
from contractor.models import Vehicles, Reviews
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
        'jobs':reversed(Jobs.objects.all()),
        'vehicles':Vehicles.objects.all(),
        "reviews":Reviews.objects.filter(customer=Customers.objects.get(id=request.session["customer_id"])),
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

def delete_job(request, job_id):
    job =Jobs.objects.get(id=job_id)

    job.delete()

    return redirect("/dashboard")

def edit_job(request, job_id):
    j=Jobs.objects.get(id=job_id)
    
    context={
        'job': j,
        'customer':Customers.objects.get(id=request.session['customer_id']),
    }
    return render(request,"edit_job.html",context)

def update_job(request, job_id):
    if 'fragile' in request.POST:
        frag=True
    else:
        frag=False
    up_job= Jobs.objects.get(id=job_id)
    
    
    up_job.title = request.POST["title"]
    up_job.start_location = request.POST["start_location"]
    up_job.end_location= request.POST["end_location"]
    up_job.description= request.POST["description"]
    up_job.attributes= request.POST['attributes']
    up_job.fragile=frag
    up_job.vehicle_type=request.POST["vehicle_type"]
    up_job.duration=timedelta(hours=int(request.POST['duration']))
    up_job.date=request.POST['date'] 
    up_job.time=request.POST["time"]  

    up_job.save()
    
    return redirect('/dashboard')

def view_job(request, job_id):
    j= Jobs.objects.get(id=job_id)
    context={
        'job':j,
        'jobs': Jobs.objects.all(),
        'customer':Customers.objects.get(id=request.session['customer_id']),
        'vehicles':Vehicles.objects.all(),
    }
    return render(request, "view_job.html", context)

def load_review_page(request,job_id): # renders the review page
    context = {
        "job": Jobs.objects.get(id=job_id),
        "customer":Customers.objects.get(id=request.session["customer_id"])
    


    }
    return render(request, "reviews.html",context)


def create_review(request): # creates a new review.
    Reviews.objects.create(
        description = request.POST['description'],
        rating = request.POST['rating'],
        customer = Customers.objects.get(id=request.session["customer_id"])
    )
    return redirect("/dashboard")   