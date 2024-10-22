from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    # Check if the request is POST (form submission)
    if request.method == 'POST':
        # Create form instance with submitted data
        form = UserCreationForm(request.POST)
        # Validate the form
        if form.is_valid():
            # Save the new user to database
            form.save()
            # Redirect to posts list page after successful registration
            return redirect('posts:list')
    else:
        # If GET request, create empty form
        form = UserCreationForm()
    
    # Context data to pass to template
    context = {
        'active_link': 'register',  # For navigation highlighting
        'form': form               # Pass form to template
    }
    
    # Render the template with context
    return render(request, 'users/register.html', context)
