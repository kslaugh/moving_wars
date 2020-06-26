from django.db import models
from user.models import Customers,Jobs
import bcrypt,re

class ContManager(models.Manager):
    def logVals(self, d):
        err={}
        u=Contractors.objects.filter(email=d['e'])
        if not u:
            err['e']='Email and/or Password incorrect'
        else:
            u=Contractors.objects.get(email=d['e'])
            if not bcrypt.checkpw(d['p'].encode(), u.password.encode()):
                err['p']='Email and/or Password incorrect'

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
        if Contractors.objects.filter(email=d['e']):
            err['ea']='Email already in use'
        if len(d['p'])<8:
            err['p']='Password needs to be at least 8 characters'
        if d['cp']!=d['p']:
            err['cp']='Passwords do not match'
        if len(d['ph1'])!=3 or len(d['ph2'])!=3 or len(d['ph3'])!=4:
            err['ph']='Please input a Valid Phone Number'
        return err
    def veVals(self,d):
        err={}
        if len(d['y'])!=4:
            err['y']='Input Vehicle Year'
        if len(d['ma'])<3:
            err['ma']='Input a proper Make'
        if len(d['mo'])<3:
            err['mo']='Please input a Model'
        if d['vt']=="default":
            err['vt']="Select a Vehicle Type"
        return err


class Contractors(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phone=models.IntegerField()
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ContManager()

class Bids(models.Model):
    amount=models.IntegerField()
    jobs=models.ForeignKey(Jobs, related_name='bids',on_delete=models.CASCADE)
    j=models.ForeignKey(Jobs,related_name='bid',on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    contractor=models.ForeignKey(Contractors, related_name='bids',on_delete=models.CASCADE)
    objects=ContManager()

class Ratings(models.Model):
    average=models.DecimalField(max_digits=3,decimal_places=2,default=5)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    contractor=models.OneToOneField(Contractors,related_name='rating',on_delete=models.CASCADE)
    objects=ContManager()

class Reviews(models.Model):
    description = models.TextField()
    rating=models.PositiveSmallIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    customer=models.ForeignKey(Customers, related_name='reviews',on_delete=models.CASCADE)
    ave_rating=models.ForeignKey(Ratings,null=True,related_name='reviews',on_delete=models.CASCADE)
    contractor=models.ForeignKey(Contractors, null=True,related_name='reviews',on_delete=models.CASCADE)
    objects=ContManager()

class Vehicles(models.Model):
    year=models.SmallIntegerField()
    make=models.CharField(max_length=255)
    model=models.CharField(max_length=255)
    vehicle_type=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(Contractors, related_name='vehicles', on_delete=models.CASCADE)
    objects=ContManager()