from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('<slug:slug>/',detail, name='book-detail'),
    
    # path('<int:id>/',detail, name='book-detail'),
]
