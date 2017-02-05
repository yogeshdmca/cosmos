from datetime import datetime, date , timedelta
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse,reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreateProfileForm,UpdateProfileForm
from .models import VehicleInfomation, FlatNumber, UserProfile


class UserHomeRedirectView(RedirectView):

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            if hasattr(self.request.user,'profile'):
                self.url = reverse_lazy('user-dashboard')
            else:
                self.url = reverse_lazy('create-profile')
        else:
            self.url = reverse_lazy('account_login')
        return super(UserHomeRedirectView, self).get(*args, **kwargs)


class NewProfile(CreateView):
    template_name = 'profile/create.html'
    model = UserProfile
    success_url = reverse_lazy('user-dashboard')
    form_class = CreateProfileForm

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super(NewProfile, self).form_valid(form)

class EditProfile(LoginRequiredMixin,UpdateView):
    template_name = 'profile/create.html'
    model = UserProfile
    success_url = reverse_lazy('user-dashboard')
    form_class = UpdateProfileForm


class dashboard(LoginRequiredMixin, View):
    template_name = 'profile/deshboard.html'
    def get(self, request, *args, **kwargs):
        profile = request.user.profile

        faimily_members = UserProfile.objects.filter(flat_number=profile.flat_number)

        ctx = {
            'faimily_members':faimily_members,
        }

        return render(request, self.template_name,ctx)


class UserLsiting(LoginRequiredMixin,ListView):
    template_name = 'profile/search.html'
    model = UserProfile
    
class VehicleInfomationView(LoginRequiredMixin,ListView):
    """docstring for VehicleInfomationView"""
    template_name = "vehicle/search.html"
    model = VehicleInfomation
    

class VehicleCreateView(LoginRequiredMixin,CreateView):
    template_name = 'vehicle/create.html'
    model = VehicleInfomation
    fields = ['serial_number','vehicle_number',]
    success_url = reverse_lazy('user-dashboard')

    def form_valid(self, form):
        vehicle = form.save(commit=False)
        vehicle.flat = self.request.user.profile.flat_number
        vehicle.added_by = self.request.user
        vehicle.save()
        return super(VehicleCreateView, self).form_valid(form)

class VehicleCreateManagerView(LoginRequiredMixin,CreateView):
    template_name = 'vehicle/create_manager.html'
    model = VehicleInfomation
    fields = ['flat','serial_number','vehicle_number',]
    success_url = reverse_lazy('vehicle-search')

    def form_valid(self, form):
        vehicle = form.save(commit=False)
        #vehicle.flat = self.request.user.profile.flat_number
        vehicle.added_by = self.request.user
        vehicle.save()
        return super(VehicleCreateView, self).form_valid(form)



class VehicleEditView(LoginRequiredMixin,UpdateView):
    template_name = 'vehicle/create.html'
    model = VehicleInfomation
    fields = ['serial_number','vehicle_number']
    success_url = reverse_lazy('user-dashboard')


class VehicleEditManagerView(LoginRequiredMixin,UpdateView):
    template_name = 'vehicle/create_manager.html'
    model = VehicleInfomation
    fields = ['flat','serial_number','vehicle_number']
    success_url = reverse_lazy('vehicle-search')

