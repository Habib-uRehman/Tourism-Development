import imp
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import HotelForm



def hotelform(request):
    
    form = HotelForm()
    if request.method == 'POST':
        # print('Printing POST' , request.POST)
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect ('/')  
            

    context = {'form' : form}

    return render(request, 'pages/hotel-form.html' , context)
      

      