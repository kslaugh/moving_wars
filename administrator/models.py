from django.db import models

# Create your models here.

class AdminManager(models.Model):
    pass
    



class Administrator(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=AdminManager()
    admin=models.ForeignKey('Administrator',null=True,on_delete=models.SET_NULL)

class Prospectors(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phone=models.IntegerField()
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=AdminManager()

class ProVehicles(models.Model):
    year=models.SmallIntegerField()
    make=models.CharField(max_length=255)
    model=models.CharField(max_length=255)
    vehicle_type=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(Prospectors,related_name='vehicles',on_delete=models.CASCADE)
    objects=AdminManager()

class NewAdmin(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=AdminManager()