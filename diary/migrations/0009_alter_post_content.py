# Generated by Django 3.2.13 on 2022-06-09 18:31

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0008_auto_20220609_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
