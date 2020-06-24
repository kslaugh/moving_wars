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
    path('logout',views.logout),
    path('del-pro/<int:id>',views.delpro),
    path('pro/<int:id>',views.viewpro),
    path('act-pro/<int:id>',views.actpro),
]