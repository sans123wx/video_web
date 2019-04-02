from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        path('' , index , name = 'index'),
        path('play_video' , play_video , name = 'play_video'),
        path('list_video' , list_video , name = 'list_video'),
        path('list_type' , list_type , name = 'list_type'),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)