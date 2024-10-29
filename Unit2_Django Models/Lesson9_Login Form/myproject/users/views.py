from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm

def register(request):
    #Check if the form is submitted
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) #submitted with data
        #validate the form
        if form.is_valid():
            form.save()
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
            return redirect("posts:list")
    else:
        form = AuthenticationForm()
    #Add bootstrap classes to the form field
    for field in form.fields.values():
        field.widget.attrs["class"] = "form-control"
        
    context = {"active_link":"login", 'form':form}
    return render(request, "users/login.html", context)