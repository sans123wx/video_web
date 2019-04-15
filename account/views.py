from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from video.models import Video_info

# Create your views here.

@login_required
def my_videos(request):
    video_infos = Video_info.objects.all()
    context = {}
    context['video_infos'] = video_infos
    return render(request , 'account/my_videos.html' , context)
