from django.urls import path
from .views import *

urlpatterns = [
    path('', starting_page, name='starting-page'),
    path('posts', posts, name='post-page'),
    path('posts/<slug:slug>', post_detail, name='post-detail-page')
]
