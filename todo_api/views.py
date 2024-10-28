from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer

# Creating a view for HTTP handling
# using ModelViewSet as it has built-in functions for handling api requests such as create, retrive, delete
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() # grab all items in Task
    serializer_class = TaskSerializer