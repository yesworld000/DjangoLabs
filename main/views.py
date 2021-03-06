from django.shortcuts import render
from main.models import Todo, Task

# Create your views here.

def todo_list(request):
    context = {
        Todo: Todo,

    }
    return render(request, 'todo_list.html', context=context)

def completed_todo_list(request):
    return render(request, 'completed_todo_list.html')