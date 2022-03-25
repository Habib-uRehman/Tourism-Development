from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('touristGuide-form/', views.touristGuideForm, name = 'touristGuideForm'),
    path('hotel-form/', views.hotelForm, name = 'hotelForm'),
]