from django.urls import path

from . import views

urlpatterns = [
    path('restraunt-form/', views.restrauntform, name = 'restraunt-form'),
]