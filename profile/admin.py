from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile, FlatNumber, VehicleInfomation, JobCategory, Event
from django.contrib import admin 
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserProfileInline(admin.TabularInline):
	model = UserProfile

class UserProfileAdmin(UserAdmin):
	inlines = [ UserProfileInline, ]
	def profile_name(self, obj):
		try:
			return obj.profile.name
		except UserProfile.DoesNotExist:
			return ''
	def mobile(self, obj):
		try:
			return obj.profile.mobile
		except UserProfile.DoesNotExist:
			return ''
	list_display = UserAdmin.list_display + ('profile_name','mobile')


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(FlatNumber)
admin.site.register(VehicleInfomation)
admin.site.register(JobCategory)
admin.site.register(Event)

