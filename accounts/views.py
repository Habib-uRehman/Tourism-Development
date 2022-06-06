from email import message
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout

def signin(request):
    if request.method == 'POST':
        # Get Form Values

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('signin')
    return render(request, 'accounts/signin.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        # Check if Password is matched
        if password == re_password:

            # check user name
            if User.objects.filter(username=username).exists():
                messages.error(request, "The user name is taken")
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is being used")
                    return redirect('signup')
                else:
                    # Every thing okay
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=name)

                    # Automatic login after registration use the below code:
                    # auth.login(request, user)
                    # messages.success(request, "You are now logged in")
                    # return redirect('index')

                    # After Registration go to login page for manual login.
                    user.save()
                    messages.success(request, "You are registered Successfully")
                    return redirect('signin')

        else:
            messages.error(request, "Password Not Matched")
            return redirect('signup')

    else:
        return render(request, 'accounts/signup.html')

# def profile(request):
#     return render(request, 'accounts/profile.html')
    

def signout(request):
    # auth.logout(request)  # logout is predefined
    # return redirect('index')
    # logout(request)
    # messages.success(request, "Logged out successfully!")
    # return redirect("index")
    auth.logout(request)
    return render(request,'index.html')