from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk') #모든 포스트를 가져옴

    return render(
        request,
        'diary/index.html',
        {
            'posts': posts,
        }
    )