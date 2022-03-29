from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('about/', views.about, name = 'about'),
    path('touristGuide-form/', views.touristGuideForm, name = 'touristGuide-form'),
    path('hotel-form/', views.hotelForm, name = 'hotelForm'),
    path('tourOperator-form/', views.tourOperatorForm, name = 'tourOperator-form'),
    path('forms/', views.forms, name = 'forms'),
]