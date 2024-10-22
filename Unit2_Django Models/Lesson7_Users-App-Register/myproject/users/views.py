from django.shortcuts import render

def register(request):
    context = {
        'active_link': 'register',
    }
    return render(request, 'users/register.html', context)
