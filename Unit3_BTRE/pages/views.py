from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse('<h1>Testing BTRE Home Page</h1>')
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')