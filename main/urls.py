from django.urls import path
from main.views import todo_list, completed_todo_list

urlpatterns = [
    path('todos/', todo_list),
    path('todos/completed/', completed_todo_list),
]
