from django.urls import path
from .views import reviews, thank_you, ReviewView

urlpatterns = [
    # path('',reviews, name='reviews'), # functional based view
    path('',ReviewView.as_view(), name='reviews'), # class based view
    path('thanks/',thank_you, name='thank-you'),
]
