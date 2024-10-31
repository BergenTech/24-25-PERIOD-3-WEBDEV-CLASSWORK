from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout

def register(request):
    #Check if the form is submitted
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) #submitted with data
        #validate the form
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list")
    else: #Get method
        form = CustomUserCreationForm()
    context = {
        'active_link': 'register',
        'form':form
    }
    return render(request, 'users/register.html', context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #LOGIN HERE
            login(request, form.get_user())
            return redirect("posts:list")
    else:
        form = AuthenticationForm()
    #Add bootstrap classes to the form field
    for field in form.fields.values():
        field.widget.attrs["class"] = "form-control"
        
    context = {"active_link":"login", 'form':form}
    return render(request, "users/login.html", context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")