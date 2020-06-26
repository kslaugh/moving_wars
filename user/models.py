from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self,post_data):
        errors= {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(post_data["first_name"]) < 2:
            errors["first_name"] = "Please enter at least 2 characters for your first first name."
        if len(post_data["last_name"]) < 2:
            errors["last_name"] = "Please enter at least 2 characters for your first last name."
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email']= "Required Valid Format"
        if len(post_data["password"]) < 8:
            errors["password"] = "Please enter at least 8 characters for your password."
        if post_data['password'] != post_data["confirm-password"]:
            errors["psw_confirm"] = "Please ensure that you password matched the confirmation"

        return errors

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
    fragile=models.BooleanField()
    vehicle_type=models.CharField(max_length=100)
    customer=models.ForeignKey(Customers, related_name='jobs', on_delete=models.CASCADE)
    duration=models.DurationField()
    date=models.DateField()
    time=models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=UserManager()