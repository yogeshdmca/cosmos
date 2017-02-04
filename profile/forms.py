from profile.models import UserProfile, FlatNumber
from django.forms import ModelForm
from django import forms

class CreateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
                'flat_number','leaving_type','name','mobile',
                'permanent_address','dob','doa','job_category','image'
            ]
    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        self.fields['flat_number'].queryset = FlatNumber.objects.filter(profiles__isnull=True)



class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
                'flat_number','leaving_type','name','mobile',
                'permanent_address','dob','doa','job_category','image'
            ]
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        #self.fields['flat_number'].queryset = FlatNumber.objects.filter(profiles__isnull=True)


class CreateProfileFormFaimily(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['leaving_type','name','mobile','dob','doa','job_category']

