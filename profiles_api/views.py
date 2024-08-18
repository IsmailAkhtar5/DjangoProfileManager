from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserProfileSerializer
from . import models
from . import permissions


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):

  queryset=models.UserProfile.objects.all()
  serializer_class=UserProfileSerializer
  authentication_classes=(JWTAuthentication,)
  permission_classes=(permissions.IsOwnIdOrReadOnly,)
  filter_backends=(SearchFilter,)
  search_fields=('name' , 'email',)
  

