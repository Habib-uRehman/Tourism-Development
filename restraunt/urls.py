from django.urls import path

from . import views

urlpatterns = [
    path('restraunt-form/', views.restrauntform, name = 'restraunt-form'),
    path('<pk>/', views.create_book, name='create-book'),
    path('gallery', views.gallery1 , name='gallery1'),
    path('gallery', views.gallery2 , name='gallery2'),
    path('gallery', views.gallery3 , name='gallery3'),
    path('gallery', views.gallery4 , name='gallery4'),
    path('gallery', views.gallery5 , name='gallery5'),
    path('gallery', views.gallery6 , name='gallery6'),
]