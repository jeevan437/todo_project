from django.shortcuts import render,render_to_response
from .models import todo_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import todo_serializer
# Create your views here.


def index_view(request):  # Define our function, accept a request

    items = todo_model.objects.all()  # ORM queries the database for all of the to-do entries.

    return render_to_response('index.html', {'items': items})
    #return render_to_response(items)


@api_view(['GET', 'POST'])
def todo_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        todo_data = todo_model.objects.all()
        serializer = todo_serializer(todo_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = todo_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)