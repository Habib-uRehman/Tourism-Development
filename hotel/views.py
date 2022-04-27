from django.shortcuts import render


def hotelform(request):
    return render(request, 'pages/hotel-form.html')