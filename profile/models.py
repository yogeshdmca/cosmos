from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings 

BLOCK = (
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),
    )

LEAVING_TYPE = (
        ('own', "My Own Home"),
        ('rent', "I am Leaving here rented"),
        ('pg', "I am Leaving here paying guest"),
    )


class FlatNumber(models.Model):
    block = models.CharField(max_length = 1, choices = BLOCK)
    number = models.IntegerField()
    
    def __str__(self):
        return str(self.number)

class JobCategory(models.Model):
    name = models.CharField("Job Category", max_length = 200)
    
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    flat_number = models.ForeignKey(FlatNumber, on_delete = models.CASCADE,
        related_name = 'flates')
    user_profile = models.ForeignKey('self', default=None)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE, related_name = 'profile')
    leaving_type = models.CharField(max_length = 40, choices = LEAVING_TYPE)
    name = models.CharField("Full Name", max_length = 200)
    mobile = models.CharField("Mobile Number", max_length = 15)
    permanent_address = models.CharField("Permanent address", max_length = 2000)
    dob = models.DateField("Date of birth")
    doa = models.DateField("Date of Anniversary")
    job_category = models.ForeignKey(JobCategory, related_name = 'profiles')
    
    def __str__(self):
        return self.name


class VehicleInfomation(models.Model):
    flat = models.ForeignKey(FlatNumber, on_delete = models.CASCADE, related_name = 'vehicles')
    serial_number = models.CharField(max_length = 30)
    vehicle_number = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.vehicle_number