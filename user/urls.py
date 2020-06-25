from django.urls import path

from .import views


urlpatterns = [
    path('',views.user),
    path('dashboard',views.dashboard),
    path('create/user',views.create_user),
    path('user/login',views.login),
    path('user/logout',views.logout),
    path('new/job',views.new_job),
    path('add/job',views.add_job),
    ]