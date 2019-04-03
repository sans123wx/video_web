from django.shortcuts import render
from .models import *

# Create your views here.
#主页
def index(request):
    list_video = Video_info.objects.filter(video_type__title = '电视剧')
    context = {}
    context['list_video'] = list_video
    return render(request , 'index.html' , context)

#分类列表
def list_type(request):
    video_type = request.GET.get('video_type')
    list_video = Video_info.objects.filter(video_type__title = video_type)
    context = {}
    context['list_video'] = list_video
    return render(request , 'list_type.html' , context)

#播放
def play_video(request):
    video_id = request.GET.get('video_id')
    video = Video.objects.get(id = video_id)
    context = {}
    context['video'] = video
    return render(request , 'play_video.html' , context)

#视频列表
def list_video(request):
    video_info_id = request.GET.get('video_info_id')
    video = Video_info.objects.get(id = video_info_id)
    context = {}
    context['video'] = video
    return render(request , 'list_video.html' , context)