from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Video_type)
class Video_typeAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Video_info)
class Video_infoAdmin(admin.ModelAdmin):
    list_display = ['video_type' , 'video_title' , 'video_detail' , 'video_img']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title' , 'video']