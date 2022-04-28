from django.urls import path

from . import views

urlpatterns = [

    path('travel-agency-form/', views.travelagencyform,  name = 'travel-agency-form'),
   
]