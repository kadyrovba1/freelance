from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import *


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateDetailSerializer
    permission_classes = (IsAuthenticated,)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)