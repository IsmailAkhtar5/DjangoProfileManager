from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):

  def create_user(self , email , name , password=None):

    if not email:
      raise ValueError("user must have an  email address")
    
    email=self.normalize_email(email)
    user=self.model(email=email , name=name)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  
  def create_superuser(self , email, name , password):

    user=self.create_user(email , name, password)
    user.is_superuser=True
    user.is_staff=True
    user.save(using=self._db)
    return user
  

class UserProfile(AbstractBaseUser , PermissionsMixin):

  name=models.CharField(max_length=255)
  email=models.EmailField(max_length=255 , unique=True)
  is_active=models.BooleanField(default=True)
  is_staff=models.BooleanField(default=False)

  objects=UserProfileManager()

  USERNAME_FIELD='email'
  REQUIRED_FIELDS=['name']

  def get_full_name(self):
    return self.name
  
  def __str__(self):
    return self.email


class UserProfileFeed(models.Model):

  user_profile=models.ForeignKey(UserProfile , on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)
  status=models.CharField(max_length=255)

  def __str__(self):

    return self.status