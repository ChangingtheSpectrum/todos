from django.shortcuts import render
from todos.models import Todo
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
from todos.serializers import TodoSerializer
 
 
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name', 'user',)
    ordering_fields = ('created',)
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
 
    def get_queryset(self):
        return Todo.objects.all().filter(user=self.request.user)
