from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index, name='index'),
    
    path('forms/', views.forms, name = 'forms'),

    path('about-us-feature/', views.aboutusfeature, name = 'about-us-feature'),

    path('about-us-overview/', views.aboutusoverview, name = 'about-us-overview'),
]