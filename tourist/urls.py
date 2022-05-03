from django.urls import path

from . import views

urlpatterns = [
    
    path('tourist-guide-form/', views.tourist, name = 'tourist-guide-form'),

]