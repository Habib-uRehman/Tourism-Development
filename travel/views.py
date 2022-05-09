import imp
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import Travelagencyform

# Create your views here.


    


def travelagencyform(request):
    
    form = Travelagencyform()
    if request.method == 'POST':
        print('Printing POST' , request.POST)
        form = Travelagencyform(request.POST)
        if form.is_valid():
            form.save()  
            return redirect ('/')  

            
    context = {'form' : form}

    return render(request, 'pages/travel-agency-form.html'  , context)    