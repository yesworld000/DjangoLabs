from django.urls import path
from main.views import ListViewSet, TaskViewSet
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('login/', obtain_jwt_token),
    
    path('todos/', ListViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('todos/<int:pk>/', ListViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'post': 'create',
                                                 'put': 'update'})),
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                                 'put': 'update'})),
    path('todos/<int:pk>/tasks/', ListViewSet.as_view({'get': 'tasks_by_list'})),
    path('todos/<int:pk>/completed/', TaskViewSet.as_view({'get': 'completed'})),
]
