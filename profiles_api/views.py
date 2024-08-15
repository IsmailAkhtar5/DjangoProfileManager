from . import models
from .serializers import UserProfileSerializer
from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):

  queryset=models.UserProfile.objects.all()
  serializer_class=UserProfileSerializer
  

