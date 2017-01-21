from profile.models import UserProfile, FlatNumber
from django.forms import ModelForm, Select, ChoiceField
from django import forms
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.admin.widgets import AdminDateWidget
from django.template import Context
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields= ['leaving_type','name','mobile','permanent_address','dob','doa','job_category']
        widgets= {
      'doa':forms.DateInput(attrs={'class':'datepicker'}),
      'dob':forms.DateInput(attrs={'class':'datepicker'}),
    }