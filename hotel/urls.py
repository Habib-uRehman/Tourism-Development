from django.urls import path

from . import views

urlpatterns = [

    path('hotel-form/', views.hotel, name = 'hotel-form'),

]