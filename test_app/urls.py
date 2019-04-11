from django.urls import path
from .views import *

urlpatterns = [
    path('' , test , name = 'test'),
    path('result/' , result , name = 'result'),
]