from django.urls import path
from .views import *

urlpatterns = [
    path('my_videos' , my_videos , name = 'my_videos'),
    path('create_video_info' , create_video_info , name = 'create_video_info'),
    path('edit_video_info' , edit_video_info , name = 'edit_video_info'),
]