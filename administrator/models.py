from django.db import models
import bcrypt,re

class AdminManager(models.Manager):
    def logVals(self, d):
        err={}
        u=Administrator.objects.filter(email=d['e'])
        if not u:
            err['e']='Email and/or Password incorrect'
        else:
            u=Administrator.objects.get(email=d['e'])
            # if not bcrypt.checkpw(d['p'].encode(), u.password.encode()):
                # err['p']='Email and/or Password incorrect'
        return err
    def regVals(self, d):
        err={}
        regex=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(d['f'])<3:
            err['f']='First Name needs to be at least 3 characters'
        if len(d['l'])<3:
            err['l']='Last Name needs to be at least 3 characters'
        if not regex.match(d['e']):
            err['e']='Invalid Email address'
        if Administrator.objects.filter(email=d['e']):
            err['ea']='Email already in use'
        if len(d['p'])<8:
            err['p']='Password needs to be at least 8 characters'
        if d['cp']!=d['p']:
            err['cp']='Passwords do not match'
        return err



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