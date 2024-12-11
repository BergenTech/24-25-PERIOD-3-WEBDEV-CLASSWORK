from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('<h1>TESTING BTRE HOME PAGE</h1>')
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')