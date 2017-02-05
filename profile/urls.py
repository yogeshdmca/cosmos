from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *
from .ajax import *

urlpatterns=[
	url(r'^$',UserHomeRedirectView.as_view(), name='home-redirect'),
	#url(r'^accounts/profile/$',NewProfile.as_view(), name='create-profile'),
    url(r'^user/create/profile/$',NewProfile.as_view(), name='create-profile'),
    url(r'^user/edit/profile/(?P<pk>\d+)/$',EditProfile.as_view(),name='edit-profile'),
    url(r'^user/dashboard/$',dashboard.as_view(), name='user-dashboard'),
    url(r'^user/listing$', UserLsiting.as_view(), name='users-listing'),
    url(r'^user/create/faimily$', create_faimily, name='users-create-faimily'),

    url(r'^user/vehicle-search/$', VehicleInfomationView.as_view(),name='vehicle-search'),
    url(r'^user/vehicle-create/$', VehicleCreateView.as_view(),name='vehicle-create'),
    url(r'^user/vehicle-edit/(?P<pk>\d+)/$', VehicleEditView.as_view(),name='vehicle-edit'),

    url(r'^user/manager/vehicle-create/$', VehicleCreateManagerView.as_view(),name='vehicle-create-manager'),
    url(r'^user/manager/vehicle-edit/(?P<pk>\d+)/$', VehicleEditManagerView.as_view(),name='vehicle-edit-manager'),

]


