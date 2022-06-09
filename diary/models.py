import os.path

from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) #새로 작성했을 때 생성
    updated_at = models.DateTimeField(auto_now=True) # 수정했을 때 생성
    head_image = models.ImageField(upload_to='diary/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='diary/files/%Y/%m/%d', blank=True)
    #author : 추후 작성


    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/diary/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)