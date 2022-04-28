from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import HotelForm



def hotelform(request):
    return render(request, 'pages/hotel-form.html')

def hotelform(request):
    
    form = HotelForm()
    if request.method == 'POST':
        print('Printing POST' , request.POST)
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect ('/')  
            

    context = {'form' : form}

    return render(request, 'pages/restraunt-form.html' , context)     