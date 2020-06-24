from django.shortcuts import render

def index(request):
    return render(request,'admin.html')

def reg(request):
    return render(request,'admin-reg.html')

