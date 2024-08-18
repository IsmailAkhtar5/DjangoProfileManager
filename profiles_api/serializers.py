from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models



class UserProfileSerializer(serializers.ModelSerializer):

  class Meta:

    model=models.UserProfile
    fields=['id' , 'email' , 'name' , 'password']
    extra_kwargs={'password':{'write_only':True}}

  def create(self , validated_data):

    user=models.UserProfile(
      name=validated_data['name'],
      email=validated_data['email']
    )  

    user.set_password(validated_data['password'])

    user.save()

    return user

class UserProfileFeedSerializer(serializers.ModelSerializer):

  class Meta:

    model=models.UserProfileFeed
    fields=['id'  , 'user_profile' , 'status' , 'created_at']
    extra_kwargs={'user_profile':{'read_only':True}}
