from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

# Create your views here.
def user(request):
    return render(request, "user.html")

def dashboard(request):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in for that")
        return redirect('/')

    context={
        'user':Customers.objects.get(id=request.session["user_id"]),
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
        email=request.POST["email"],
        password=hashed_pw,
    )

    request.session["user_id"] = created_user.id
    
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
        request.session['user_id'] = potential_users[0].id
        return redirect('/dashboard')

    messages.error(request, "Please check you email and Password")
    return redirect ('/')