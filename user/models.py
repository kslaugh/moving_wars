from django.db import models


class UserManager(models.Manager):
    pass


class Customers(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    contact_meth=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=UserManager()

class Jobs(models.Model):
    title=models.CharField(max_length=255)
    start_location=models.CharField(max_length=100)
    end_location=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    attributes=models.CharField(max_length=100)
    vehicle_type=models.CharField(max_length=100)
    customer=models.ForeignKey(Customers, related_name='jobs', on_delete=models.CASCADE)
    duration=models.DurationField()
    date=models.DateField()
    time=models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=UserManager()