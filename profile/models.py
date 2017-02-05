from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings 
from cloudinary.models import CloudinaryField

BLOCK = (
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),
    )

RESIDENT_TYPE = (
        ('own', "Home owner"),
        ('spouse', "Wife"),
        ('son', "Son"),
        ('daughter', "Daughter"),
        ('father', "Father"),
        ('mother', "Mother"),
        ('faimily', "My Faimily member"),
        ('rent', "Rented Member"),
    )


class FlatNumber(models.Model):
    block = models.CharField(max_length = 1, choices = BLOCK)
    number = models.IntegerField()

    @property
    def get_block(self):
        return dict(BLOCK).get(self.block)

    def get_flat_number(self):
        return "%s-%s"%(self.get_block, self.number)
    
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
    leaving_type = models.CharField("Resident Type",max_length = 40, choices = RESIDENT_TYPE)
    name = models.CharField("Full Name", max_length = 200)
    mobile = models.CharField("Mobile Number", max_length = 15)
    permanent_address = models.CharField("Permanent address. if have?", max_length = 2000,null=True, blank=True)
    dob = models.DateField("Date of birth",null=True, blank=True)
    doa = models.DateField("Date of Anniversary",null=True, blank=True)
    job_category = models.ForeignKey(JobCategory, related_name = 'profiles')
    image = CloudinaryField('Photo',null=True, blank=True)
    
    def __str__(self):
        return self.name

    def get_vehicle_information(self):
        return self.flat_number.vehicles.all()

    def ge_resident_type(self):
        if self.leaving_type=='rent':
            return "On Rented"
        else:
            return "Owner"


class VehicleInfomation(models.Model):
    flat = models.ForeignKey(FlatNumber, on_delete = models.CASCADE, related_name = 'vehicles')
    serial_number = models.CharField(max_length = 30)
    vehicle_number = models.CharField(max_length = 20)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='chields')
    amount = models.FloatField("Amount collected", default=0.0)

    def get_flat_vehicle_names(self):
        return ", ".join([name.name for name in self.flat.profiles.filter(leaving_type__in=['own','rent'])])
    
    def __str__(self):
        return self.vehicle_number

    @property
    def get_type(self):
        if self.serial_number.startswith('c'):
            return 'car'
        else:
            return 'bike'


class Event(models.Model):
    title = models.CharField(max_length = 200)
    details = models.CharField(max_length = 20)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='events')
    date = models.DateTimeField("Date of birth")
    image = CloudinaryField('Event Image')
    
    def __str__(self):
        return self.title
