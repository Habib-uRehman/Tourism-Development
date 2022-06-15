import imp
from django.shortcuts import render , redirect
from django.http import HttpResponse

from . models import myuploadfile



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
    context = {
        "data":myuploadfile.objects.all(),
    }
    return render(request,"pages/test.html",context)


def send_files(request):
    if request.method == "POST" :
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfoles")
        
        for f in myfile:
            myuploadfile(f_name=name,myfiles=f).save()
        
        return redirect("fileapp:index")

                

