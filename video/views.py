from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    list_video = Video_info.objects.filter(video_type__title = '电视剧')
    context = {}
    context['list_video'] = list_video
    return render(request , 'index.html' , context)

def play_video(request):
    video_id = request.GET.get('video_id')
    video = Video.objects.get(id = video_id)
    context = {}
    context['video'] = video
    return render(request , 'play_video.html' , context)
