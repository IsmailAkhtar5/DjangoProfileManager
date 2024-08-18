from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import serializers
from . import models
from . import permissions


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):

  queryset=models.UserProfile.objects.all()
  serializer_class=serializers.UserProfileSerializer
  authentication_classes=(JWTAuthentication,)
  permission_classes=(permissions.IsOwnIdOrReadOnly,)
  filter_backends=(SearchFilter,)
  search_fields=('name' , 'email',)


class UserProfileFeedViewSet(viewsets.ModelViewSet):

  queryset=models.UserProfileFeed.objects.all()
  serializer_class=serializers.UserProfileFeedSerializer
  authentication_classes=(JWTAuthentication,)
  

  def perform_create(self, serializer):
    
    serializers.save(user_profile=self.request.user)