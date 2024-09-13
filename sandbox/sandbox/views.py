from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello BT! Welcome to HomePage!")

def about(request):
    return HttpResponse("All about me!")