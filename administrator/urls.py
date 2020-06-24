from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('reg',views.reg),
    path('register',views.register),
    path('login',views.log),
    path('home',views.home),
    path('accept-admin/<int:id>',views.actadmin),
    path('deny-admin/<int:id>',views.denadmin),
    path('del-admin/<int:id>',views.deladmin),
]