from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()[:10]

    objs = {
        'todos':todos
    }

    return render(request, 'index.html', objs)

def details(request, id):
    todo = Todo.objects.get(id=id)

    objs = {
        'todo':todo
    }

    return render(request, 'details.html', objs)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/')
    else:
        return render(request, 'add.html')