from django.urls import path

from . import views

urlpatterns = [
    path('restraunt-form/', views.restrauntform, name = 'restraunt-form'),
    # path('<pk>/', views.create_book, name='create-book'),
    path('Ziarat', views.gallery1 , name='gallery1'),
    path('Khuzdar', views.gallery2 , name='gallery2'),
    path('Gawadar', views.gallery3 , name='gallery3'),
    path('Peer Ghayb', views.gallery4 , name='gallery4'),
    path('Bolan', views.gallery5 , name='gallery5'),
    path('Gadani Beach', views.gallery6 , name='gallery6'),
]