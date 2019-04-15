from django.urls import path
from .views import *

urlpatterns = [
    path('my_videos' , my_videos , name = 'my_videos'),
]