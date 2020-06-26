from django.urls import path

from .import views

urlpatterns=[
    path('', views.index),
    path('login', views.log),
    path('reg', views.reg),
    path('register', views.register),
    path('home',views.home),
    path('add/vehicle',views.addv),
    path('update/vehicles',views.addvehicle),
    path('logout',views.logout),
    path('<int:id>',views.viewjob),
    path('cancel',views.cancel),
    path('<int:id>/bid',views.bid),
    path('<int:id>/placebid',views.placebid),
]