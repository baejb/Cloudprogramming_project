# Generated by Django 3.2.13 on 2022-06-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_post_head_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='diary/files/%Y/%m/%d'),
        ),
    ]