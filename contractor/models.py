from django.db import models
from user.models import Customers,Jobs

class ContManager(models.Manager):
    pass


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
    job=models.ForeignKey(Jobs, related_name='bids',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    contractor=models.ForeignKey(Contractors, related_name='bids',on_delete=models.CASCADE)
    objects=ContManager()

class Ratings(models.Model):
    average=models.DecimalField(max_digits=3,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    contractor=models.OneToOneField(Contractors,related_name='rating',on_delete=models.CASCADE)
    objects=ContManager()

class Reviews(models.Model):
    rating=models.PositiveSmallIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    customer=models.ForeignKey(Customers, related_name='reviews',on_delete=models.CASCADE)
    ave_rating=models.ForeignKey(Ratings,related_name='reviews',on_delete=models.CASCADE)
    contractor=models.ForeignKey(Contractors,related_name='reviews',on_delete=models.CASCADE)
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