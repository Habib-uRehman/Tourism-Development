import imp
from django.shortcuts import render

from django.http import HttpResponse

def index(request):

    return render(request, 'pages/index.html')

def about(request):
    
    return render(request, 'pages/about.html')

def touristGuideForm(request):
    return render(request, 'pages/touristGuide-form.html')

def hotelForm(request):
    return render(request, 'pages/hotel-form.html')

