from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import CommentForm
from .models import Post, Category, Tag


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

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload', 'category', 'tags']
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/diary/')

class PostList(ListView):
    model = Post
    ordering = '-pk'
    #template_name = 'diary/index.html' 템플릿 강제

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context


def single_post_pages(request, pk):
    post = Post.objects.get(pk='pk')



    return render(
        request,
        'diary/post_detail.html',
        {
            'post': post,
        }
    )


def categories_page(request, slug):
    if slug == 'no-category':
        category = '감정X'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    context = {
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count(),
        'category': category,
        'post_list': post_list
    }
    return render(request, 'diary/post_list.html', context)

def show_tag_posts(request, slug):
    tag = Tag.objects.get(slug = slug)
    post_list = tag.post_set.all()

    context = {
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count(),
        'tag' : tag ,
        'post_list' : post_list
    }
    return render(request, 'diary/post_list.html' , context)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload', 'category']

    template_name = "diary/post_form_update.html"
    def dispatch(self, request, *args, **kwargs):
        current_user = request.user
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request,*args,**kwargs)
        else:
            raise PermissionDenied
def add_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
            else:
                return redirect(post.get_absolute_url())

    else:
        raise PermissionDenied