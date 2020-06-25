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
    path('delete/<int:job_id>/',views.delete_job),
    path('edit/<int:job_id>/',views.edit_job),
    path('edit/<int:job_id>/update',views.update_job),
    path('view/<int:job_id>/', views.view_job),

    ]