# serializing models

from rest_framework import serializers
from .models import Todo, TodoStatus


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'status', 'task_date']


class TodoStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoStatus
        fields = ['id', 'status_name']
