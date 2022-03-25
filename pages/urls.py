from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('touristguideform', views.touristguideform, name = 'touristguideform')
]