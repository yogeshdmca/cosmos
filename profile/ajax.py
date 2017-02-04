import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.forms import SignupForm
from .forms import CreateProfileFormFaimily


class CreateFaimily(LoginRequiredMixin, View):
    template_name = 'ajax/create_faimily.html'
    def get(self, request, *args, **kwargs):
        form = CreateProfileFormFaimily()
        login_form = SignupForm()
        return render(request, self.template_name, {"form":form,'login_form':login_form})

    def post(self, request, *args, **kwargs):
        form = CreateProfileFormFaimily(request.POST)
        login_form = SignupForm(request.POST)
        if form.is_valid() and login_form.is_valid():
            user = login_form.save(request)
            profile = form.save(commit=False)
            profile.user = user
            profile.parent = request.user.profile
            profile.flat_number = request.user.profile.flat_number
            profile.permanent_address = request.user.profile.permanent_address
            profile.save()
            return HttpResponse(json.dumps({"sucess": 'true'}),status=200,content_type="application/json")
        return render(request,self.template_name, {"form":form,'login_form':login_form})
        #responce = render_to_string(self.template_name, {"form":form,'login_form':login_form})
        #return HttpResponse(json.dumps({"sucess": 'data','responce':responce}),content_type="application/json")

create_faimily = CreateFaimily.as_view()