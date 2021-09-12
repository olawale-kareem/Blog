from django.urls import path
from .views import *

urlpatterns = [
    # static url
    # path('january/', jan, name='jan'),
    # path('feburary/', feb, name='feb'),

    # dynamic url
    # url format
    path('', challenge_list, name='challenge_list'),
    path('<int:month>/', monthly_challenge_by_number, name='monthly-challenges_by_num'),
    path('<str:month>/', monthly_challenge, name='monthly-challenges')
]
