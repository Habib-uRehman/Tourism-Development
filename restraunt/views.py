from multiprocessing import context
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RestrauntForm


def restrauntform(request):
    
    form = RestrauntForm()
    if request.method == 'POST':
        # print('Printing POST' , request.POST)
        form = RestrauntForm(request.POST)
        if form.is_valid():
            form.save()    
            return redirect ('/')

    context = {'form' : form}

    return render(request, 'pages/restraunt-form.html' , context)  



def gallery1(request):
    return render (request, 'pages/gallery1.html' )    


def gallery2(request):
    return render (request, 'pages/gallery2.html' ) 


def gallery3(request):
    return render (request, 'pages/gallery3.html' ) 



def gallery4(request):
    return render (request, 'pages/gallery4.html' ) 


def gallery5(request):
    return render (request, 'pages/gallery5.html' ) 


def gallery6(request):
    return render (request, 'pages/gallery6.html' ) 