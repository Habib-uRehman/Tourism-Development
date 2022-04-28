import imp
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')


def forms(request):
    return render(request, 'pages/forms.html')    

def aboutusfeature(request):
    return render (request, 'pages/about-us-feature.html')      



def aboutusoverview(request):
    return render (request, 'pages/about-us-overview.html') 

      