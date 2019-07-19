from django.urls import path
from .views import *
urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>', TaskDetailView.as_view(), name='detail'),
    path('<int:pk>/order', OrderCreate.as_view(), name='order'),

    ]