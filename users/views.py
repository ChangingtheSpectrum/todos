from django.shortcuts import render
from users.models import User

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import filters

from users.serializers import UserSerializer
from . import permissions
 
 
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('username', 'email',)
    ordering_fields = ('id',)
 
 
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
 
    def get_queryset(self):
        return User.objects.all().filter(username=self.request.user)