from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def restrauntform(request):
    return render(request, 'pages/restraunt-form.html')  