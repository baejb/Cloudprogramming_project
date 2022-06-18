from django.shortcuts import render

# Create your views here.
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()

    return render(request, 'todolist/todo_list.html', {'todos': todos})