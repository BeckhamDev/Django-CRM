from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # Check to see if the user is logged in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Authenticating the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "User logged in")
            return redirect('home')
        else:
            messages.error(request, "There was a problem authenticating the user, please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "User logged out")
    return redirect('home')
