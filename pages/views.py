import imp
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')


# def touristGuideForm(request):
#     return render(request, 'pages/touristGuide-form.html')

# def hotelForm(request):
#     return render(request, 'pages/hotel-form.html')


# def tourOperatorForm(request):
#     return render(request, 'pages/tourOperator-form.html')

def forms(request):
    return render(request, 'pages/forms.html')    


def travelagencyform(request):
    return render(request, 'pages/travel-agency-form.html')    


def restrauntform(request):
    return render(request, 'pages/restraunt-form.html')   


def hotelform(request):
    return render(request, 'pages/hotel-form.html') 


def aboutusfeature(request):
    return render (request, 'pages/about-us-feature.html')      



def aboutusoverview(request):
    return render (request, 'pages/about-us-overview.html') 

      