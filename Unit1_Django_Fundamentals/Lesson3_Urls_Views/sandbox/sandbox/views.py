from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello BT! Welcome to HomePage!")
    return render(request, 'home.html')
def about(request):
    # return HttpResponse("All about me!")
    return render(request, 'about.html')