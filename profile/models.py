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
        ('own', "Home owner"),
        ('faimily', "My Faimily member"),
        ('rent', "rented"),
        ('pg', "I am Leaving here paying guest"),
    )


class FlatNumber(models.Model):
    block = models.CharField(max_length = 1, choices = BLOCK)
    number = models.IntegerField()

    def get_block(self):
        return dict(BLOCK).get(self.block)
    
    def __str__(self):
        return "%s-%s"%(self.block, self.number)

class JobCategory(models.Model):
    name = models.CharField("Job Category", max_length = 200)
    
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    flat_number = models.ForeignKey(FlatNumber,related_name = 'profiles')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='chields')
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name = 'profile')
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
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='chields')
    amount = models.FloatField("Amount collected", default=0.0)
    
    def __str__(self):
        return self.vehicle_number
