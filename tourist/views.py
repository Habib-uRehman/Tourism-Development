import imp
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import Touristguideform
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def tourist(request):
    
    form = Touristguideform()
    if request.method == 'POST':
        print('Printing POST' , request.POST)
        form = Touristguideform(request.POST)
        if form.is_valid():
            form.save()  
            return redirect ('/')  

            
    context = {'form' : form}

    return render(request, 'pages/tourist-guide-form.html' , context)   


