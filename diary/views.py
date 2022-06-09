from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from .models import Post
# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk') #모든 포스트를 가져옴
#
#     return render(
#         request,
#         'diary/index.html',
#         {
#             'posts': posts,
#         }
#     )
class PostList(ListView):
    model = Post
    #template_name = 'diary/index.html' 템플릿 강제

class PostDetail(DetailView):
    model = Post

def single_post_pages(request, pk):
    post = Post.objects.get(pk=pk)


    return render(
        request,
        'diary/post_detail.html',
        {
            'post': post,
        }
    )