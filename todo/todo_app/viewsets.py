from rest_framework import viewsets,generics
from .serializers import todo_serializer
from .models import todo_model

class Todo_ViewSet(viewsets.ModelViewSet):
    serializer_class = todo_serializer
    queryset = todo_model.objects.all()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = todo_model.objects.all()
    serializer_class = todo_serializer