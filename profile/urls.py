from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *

urlpatterns=[
	url(r'^$',UserHomeRedirectView.as_view(), name='home-redirect'),
	#url(r'^accounts/profile/$',NewProfile.as_view(), name='create-profile'),
    url(r'^user/create/profile/$',NewProfile.as_view(), name='create-profile'),
    url(r'^user/dashboard/$',dashboard.as_view(), name='user-dashboard'),
    url(r'^user/listing$', ShowUsers.as_view(), name='users-listing'),
    url(r'^user/create-new-user/$', AddUser.as_view(), name='add-user'),
    url(r'^user/vehicle-search/$', VehicleInfomationView.as_view(),name='vehicle-search'),
    url(r'^user/vehicle-create/$', VehicleCreateView.as_view(),name='vehicle-create'),
    url(r'^user/profile/$', Profile.as_view(),name='user-profile'),
    
    #url(r'^search/info/$', ajax.ajax_search_by, name='vehicle-search-ajax'),
    
]