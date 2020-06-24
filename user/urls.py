from django.urls import path

from .import views


urlpatterns = [
    path('',views.user),
    path('create/user',views.create_user),
    path('user/login',views.login),
    ]