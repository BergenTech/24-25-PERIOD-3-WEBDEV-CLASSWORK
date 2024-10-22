from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    #Check if the form is submitted
    if request.method == "POST":
        form = UserCreationForm(request.POST) #submitted with data
        #validate the form
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else: #Get method
        form = UserCreationForm()
    context = {
        'active_link': 'register',
        'form':form
    }
    return render(request, 'users/register.html', context)
