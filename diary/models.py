import os.path

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from markdownx.utils import markdown
from markdownx.models import MarkdownxField


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/diary/tag/{self.slug}/'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural : 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/diary/category/{self.slug}/'

class Post(models.Model):
    title = models.CharField(max_length=30)
    tags = models.ManyToManyField(Tag, blank=True)
    content = MarkdownxField()
    hook_msg = models.TextField(blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL )
    created_at = models.DateTimeField(auto_now_add=True) #새로 작성했을 때 생성
    updated_at = models.DateTimeField(auto_now=True) # 수정했을 때 생성
    head_image = models.ImageField(upload_to='diary/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='diary/files/%Y/%m/%d', blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f'[{self.pk}]{self.title} : {self.author}'

    def get_absolute_url(self):
        return f'/diary/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_content_markdown(self):
        return markdown(self.content)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'