from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task
from .serializers import *


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

class OrderCreate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save(executor=self.request.user)