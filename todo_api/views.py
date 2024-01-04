from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Todo, TodoStatus
from .serializers import TodoSerializer, TodoStatusSerializer
from rest_framework import viewsets

# Create your views here.


# converting to class-based views
class TodoViewSet(viewsets.ModelViewSet):
    """
    A todo viewset that handles most of the proprietary endpoint methods (create, retrieve, update, list, etc)
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# @api_view(['GET', 'POST'])
# def todos_list(request, format=None):
#     """
#     Get a list of all todos
#     """
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'DELETE', 'PUT'])
# def todo_detail(request, pk):
#     """
#     Perform operations on individual todo items
#     """

#     # check if the item exists
#     try:
#         todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'DELETE':
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
