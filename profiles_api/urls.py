
from rest_framework import routers
from django.urls import path , include
from . import views

router=routers.DefaultRouter()
router.register("profile" , views.UserProfileViewSet , basename="userprofile" )
urlpatterns = [

    path('' ,  include(router.urls))
]
