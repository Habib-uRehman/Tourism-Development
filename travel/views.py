import imp
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def travelagencyform(request):
    return render(request, 'pages/travel-agency-form.html')    