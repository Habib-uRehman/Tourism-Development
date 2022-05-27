from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.index, name='index'),
    
    path('forms/', views.forms, name = 'forms'),

    path('about-us-feature/', views.aboutusfeature, name = 'about-us-feature'),

    path('about-us-overview/', views.aboutusoverview, name = 'about-us-overview'),

    path('contactus/', views.contactus, name = 'contactus'),

    path('profile/', views.profile, name = 'profile'),

    path('test/', views.test, name = 'test'),

    path('signup/', views.signup, name = 'signup'),

    path('signin/', views.signin, name = 'signin'),


]