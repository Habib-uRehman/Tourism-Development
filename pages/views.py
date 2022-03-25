import imp
from django.shortcuts import render

from django.http import HttpResponse

def index(request):

    return render(request, 'pages/index.html')

def touristguideform(request):
    
    return render(request, 'pages/touristGuide-form.html')


