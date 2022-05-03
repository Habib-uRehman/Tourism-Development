import imp
from django.shortcuts import render

from django.http import HttpResponse

def tourist(request):
    return render(request, 'pages/tourist-guide-form.html')