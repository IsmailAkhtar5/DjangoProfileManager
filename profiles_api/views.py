from django.shortcuts import render 
from rest_framework import viewsets , status 
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from . import serializers
from . import models
from . import permissions
from .import  pagination


# Create your views here.
class LoginViewSet(viewsets.ViewSet):

  serializer_class=AuthTokenSerializer

  def create(self , request):
    
    serializer = self.serializer_class(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)


class UserProfileViewSet(viewsets.ModelViewSet):

  queryset=models.UserProfile.objects.all()
  serializer_class=serializers.UserProfileSerializer
  authentication_classes=(TokenAuthentication,)
  permission_classes=(permissions.IsOwnIdOrReadOnly,)
  pagination_class=pagination.DefaultPagination
  filter_backends=(SearchFilter,)
  search_fields=('name' , 'email',)


class UserProfileFeedViewSet(viewsets.ModelViewSet):

  queryset=models.UserProfileFeed.objects.all()
  serializer_class=serializers.UserProfileFeedSerializer
  authentication_classes=(TokenAuthentication,)
  permission_classes=(permissions.PostOwnStatus , IsAuthenticatedOrReadOnly)
  pagination_class=pagination.DefaultPagination
  

  def perform_create(self, serializer):
    
    serializer.save(user_profile=self.request.user)