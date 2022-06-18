from django.shortcuts import render

# Create your views here.
def main_pages(request):
    #post = Post.objects.get(pk='pk')

    return render(request, 'diary_main_pages/index.html')

