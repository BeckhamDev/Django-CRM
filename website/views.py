from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingUpForm
from .models import Record


def home(request):
    # Showing the records
    records = Record.objects.all()
    
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
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "User logged out")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticating and logging in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "User Successfully Registered")
            return redirect('home')
    else:
        form = SingUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})
