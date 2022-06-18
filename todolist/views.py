from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'todolist/index.html', content)


def createTodo(request):
    user_input_str = request.POST['todoContent']    # name값이 todoContent였지!
    new_todo = Todo(content = user_input_str)       # DB의 Todo테이블에 쓰고,
    new_todo.save()                                 # 저장!
    return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한todo의 id", done_todo_id)
    todo = Todo.objects.get(id=done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id",done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))