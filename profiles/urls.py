from django.urls import path

from .views import *

urlpatterns = [
    # path('', index, name='index-page'),
    path('', CreateProfileView.as_view(), name='create-profile'),
    path('profile-list/', ProfilesView.as_view(), name='profile-list')
 
]
