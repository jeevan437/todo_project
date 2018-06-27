from rest_framework import viewsets
from .serializers import todo_serializer
from .models import todo_model

class Todo_ViewSet(viewsets.ModelViewSet):
    serializer_class = todo_serializer
    queryset = todo_model.objects.all()