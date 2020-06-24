from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('reg',views.reg),
    path('register',views.register),
    path('login',views.log),
    path('home',views.home),
    path('accept-admin',views.actadmin),
    path('deny-admin',views.denadmin),
]