from django.urls import path

from . import views

urlpatterns = [
    path('restraunt-form/', views.restrauntform, name = 'restraunt-form'),
    path('<pk>/', views.create_book, name='create-book')
]