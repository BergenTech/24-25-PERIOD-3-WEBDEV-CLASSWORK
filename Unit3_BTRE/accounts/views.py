from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        #Login User
        return
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def register(request):
    if request.method == "POST":
        #Register User
        messages.error(request, "Testing Error Messages!")
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')