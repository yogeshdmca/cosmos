from datetime import datetime, date , timedelta
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse,reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from profile.models import FlatNumber, UserProfile
from django import forms
from .forms import UserProfileForm
from .models import VehicleInfomation
from allauth.account.forms import SignupForm
from django.contrib.auth.mixins import LoginRequiredMixin



class VehicleInfomationView(ListView):
    """docstring for VehicleInfomationView"""
    template_name = "profile/vehicle_search.html"
    model = VehicleInfomation

        

class UserHomeRedirectView(RedirectView):

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            if hasattr(self.request.user,'profile'):
                self.url = reverse_lazy('user-profile')
            else:
                self.url = reverse_lazy('create-profile')
        else:
            self.url = reverse_lazy('account_login')
        return super(UserHomeRedirectView, self).get(*args, **kwargs)



class VehicleCreateView(CreateView):
    template_name = 'profile/vehicle_create.html'
    model = VehicleInfomation
    fields = ['flat','serial_number','vehicle_number','amount']
    success_url = reverse_lazy('vehicle-search')
    def form_valid(self, form):
        #import pdb;pdb.set_trace()
        vehicle = form.save(commit=False)
        vehicle.user = self.request.user
        vehicle.save()
        #return vehicle
        return super(VehicleCreateView, self).form_valid(form)


class NewProfile(CreateView):
    template_name = 'profile/new_profile.html'
    model = UserProfile
    fields = [
        'flat_number','leaving_type','name','mobile',
        'permanent_address','dob','doa','job_category',
    ]
    widgets= {
      'doa':forms.DateInput(attrs={'class':'datepicker'}),
      'dob':forms.DateInput(attrs={'class':'datepicker'}),
    }
    success_url = reverse_lazy('user-dashboard')
    
    def form_valid(self, form):
        #import pdb;pdb.set_trace()
        self.new_user = form.save(commit=False)
        self.new_user.user = self.request.user
        self.new_user.save()
        return super(NewProfile, self).form_valid(form)
        

class Profile(TemplateView):
    """docstring for TemplateView"""
    template_name = "profile/profile.html"


class dashboard(LoginRequiredMixin, View):
    template_name = 'profile/deshboard.html'
    def get(self, request, *args, **kwargs):
        user = request.user.profile
        birthdays = UserProfile.objects.filter(dob=date.today())
        upcomming_bdays = UserProfile.objects.filter(dob__gt=date.today(),dob__lte=date.today()+timedelta(days=5))
        anniversaries = UserProfile.objects.filter(doa=date.today())

        ctx = {
            'birthdays':birthdays,
            'upcomming_bdays':upcomming_bdays,
            'anniversaries':anniversaries,

        }
        return render(request, self.template_name,ctx)

class UserLsiting(ListView):
    template_name = 'profile/users_listing.html'
    model = UserProfile
    

class AddUser(LoginRequiredMixin, View):
    template_name = 'profile/add_new_user.html'
    def get(self, request, *args, **kwargs):
        user_form = SignupForm()
        profile_form = UserProfileForm()
        return render(request, self.template_name, {'user_form':user_form,
            'profile_form':profile_form})

    def post(self, request, *args, **kwargs):
        user_form = SignupForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(request)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user.is_active = True
            user.save()
            return HttpResponseRedirect(reverse('users-listing'))
        return render(request, self.template_name, {'user_form':user_form,
            'profile_form':profile_form})

