from django.urls import path
from .views import *
urlpatterns = [
    path('task/', TaskCreateView.as_view(), name='task'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
]