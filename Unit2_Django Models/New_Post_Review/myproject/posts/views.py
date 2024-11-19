from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
# from django.http import HttpResponse


# Create your views here.
@login_required(login_url="/users/login")
def posts_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.all().order_by('date')
    context = {
        'active_link': 'posts',
        'posts':posts
    }
    return render(request,'posts/posts_list.html', context)
def post_page(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html',{'post':post} )

@login_required(login_url="/users/login")
def new_post(request):
    form = forms.CreatePost()
    return render(request, "posts/new_post.html", {'form':form})