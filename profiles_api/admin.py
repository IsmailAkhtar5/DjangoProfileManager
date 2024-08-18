from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header="Admin Interface"
admin.site.index_title="User Profile Administration "

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
  
  search_fields=['email']
  search_help_text="search result by email"
  list_display=['id' , 'name' ,'email' , 'is_active' ,'is_staff']
  list_per_page=10
  list_filter=['email']
  ordering=['id' , 'name' ,'is_active' , 'is_staff']

@admin.register(models.UserProfileFeed)
class UserProfileFeedAdmin(admin.ModelAdmin):
  
  ordering=['status' , 'created_at']
  list_display=['user_profile' , 'status' , 'created_at']
  list_filter=['user_profile']
  list_editable=['status']
  list_per_page=10

  