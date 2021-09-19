from django.urls import path
from .views import *

urlpatterns = [ 
    # functional based or generic view
    # path('',reviews, name='reviews'), 
    # path('thanks/',thank_you, name='thank-you'), 

    # class based view
    path('',ReviewView.as_view(), name='reviews-class'),               #base view
    path('thanks/',ThankYouView.as_view(), name='thank-you-class'),    #base view

    path('thanks2/',ThankYou.as_view(), name='thank-you-temp' ),       #Template view
    path('review_list/',ReviewsList.as_view(), name='review-list' ),   #Template view
    # path('single_review/<int:id>',SingleDetail.as_view(), name='single-detail' ), # Template view

    path('favorite/', AddFavoriteView.as_view(), name='fav-view'),
    path('single_review/<int:pk>', SingleDetail.as_view(), name='single-detail' ), # detailview, note 'pk' is used as a 
                                                                                   # variable in the url placeholder 
]
