from django.shortcuts import render

# Create your views here.
def login(request):
    if request.get == "POST":
        #Login User
        return
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def register(request):
    if request.get == "POST":
        #Register User
        return
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')