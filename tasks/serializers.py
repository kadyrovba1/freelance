from django.db import transaction
from rest_framework import serializers

from tasks.models import Task
#from users.models import Transaction

class TaskCreateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'price', 'created_time', 'created_by', 'executor')


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'price', 'created_time', 'created_by', 'executor', 'ready')
