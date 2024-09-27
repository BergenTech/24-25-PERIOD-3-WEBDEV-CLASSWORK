from django.shortcuts import render

# Create your views here.
def posts_list(request):
    context = {
        'active_link': 'posts'
    }
    return render(request,'posts/posts_list.html', context)