from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from contacts.models import Contact

# Create your views here.
def login(request):
    if request.method == "POST":
        #Login User
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password )
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are successfully logged in!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Credentials! Try Again!")
            return redirect("login")
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out!")
        return redirect("index")
    # else:
    #     messages.error(request, "You have to login first!")
    #     return redirect("index")

def register(request):
    if request.method == "POST":
        #Register User
        # messages.error(request, "Testing Error Messages!")
        # Get the data from the form fields
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # password match
        if password != password2:
            messages.error(request,"Passwords dont match!")
            return redirect('register')
        else:
            # check if username is not taken
            if User.objects.filter(username=username).exists():
                messages.error(request,"That username is taken!")
                return redirect('register')
            else:
                # check if email is already used
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is being used!")
                    return redirect('register')
                else:
                    # Everything looks good!
                    newUser = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name )
                    # save the new user to the database
                    newUser.save()
                    messages.success(request, "You are now registered and can log in!")
                    return redirect('login')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    user_inquiries = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'inquiries': user_inquiries
    }
    return render(request, 'accounts/dashboard.html', context)
