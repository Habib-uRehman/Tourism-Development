import imp
from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm


def index(request):
    return render(request, 'pages/index.html')


def forms(request):
    return render(request, 'pages/forms.html')    

def aboutusfeature(request):
    return render (request, 'pages/about-us-feature.html')      

def challan(request):
    return render (request, 'pages/challan.html')      


def aboutusoverview(request):
    return render (request, 'pages/about-us-overview.html') 

def contactus(request):
    return render (request, 'pages/contactus.html')   


def profile(request):
    return render (request, 'pages/profile.html')      



def test(request):
    return render (request, 'pages/test.html')  



                


def create_book_form(request):
    form = BookForm()
    context = {
        "form": form
    }
    return render(request, "partials/book_form.html", context)    