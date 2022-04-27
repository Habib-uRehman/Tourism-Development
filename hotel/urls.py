from django.urls import path

from . import views


urlpatterns = [
    path('hotel-form/', views.hotelform, name = 'hotel-form'),
]