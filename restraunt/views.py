from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RestrauntForm


def restrauntform(request):
    
    form = RestrauntForm()

    context = {'form' : form}

    return render(request, 'pages/restraunt-form.html' , {'form' :form})  


# def updateUser(request):
#     user = request.user
#     form = UserForm(instance=user)

#     if request.method == 'POST':
#         form = UserForm (request.POST ,request.FILES, instance=user) 
#         if form.is_valid():
#            form.save()
#            return redirect('user-profile' , pk=user.id)

#     return render (request, 'base/update-user.html' , {'form' :form} ) 




# def create_book(request, pk):
#     author = Author.objects.get(id=pk)
#     books = Book.objects.filter(author=author)
#     formset = BookFormSet(request.POST or None)

#     if request.method == "POST":
#         if formset.is_valid():
#             formset.instance = author
#             formset.save()
#             return redirect("create-book", pk=author.id)

#     context = {
#         "formset": formset,
#         "author": author,
#         "books": books
#     }

#     return render(request, "create_book.html", context)    


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