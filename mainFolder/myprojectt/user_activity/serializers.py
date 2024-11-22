from rest_framework import serializers
from .models import RequestLog, Task


class RequestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLog
        fields = '__all__'  # Include all fields from the RequestLog model


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']  # Specify the fields you want to include
