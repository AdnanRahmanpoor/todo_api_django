from rest_framework import serializers
from .models import Task

# Serializer converts a model (Task in this instance) to a JSON format which will be shown in the API test
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed']