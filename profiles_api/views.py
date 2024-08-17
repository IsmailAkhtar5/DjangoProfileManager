from django.shortcuts import render
from rest_framework import viewsets 
from  rest_framework.authentication import TokenAuthentication
from .serializers import UserProfileSerializer
from . import models
from . import permissions


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):

  queryset=models.UserProfile.objects.all()
  serializer_class=UserProfileSerializer
  authentication_classes=(TokenAuthentication,)
  permission_classes=(permissions.IsOwnIdOrReadOnly,)
  

