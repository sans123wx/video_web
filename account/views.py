from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from video.models import Video_info
from django.http import HttpResponse
from .forms import *

# Create your views here.

@login_required
def my_videos(request):
    video_infos = Video_info.objects.all()
    context = {}
    context['video_infos'] = video_infos
    return render(request , 'account/my_videos.html' , context)

@login_required
def create_video_info(request):
    if request.method == 'POST':
        form = Video_infoForm(request.POST)
        upload_image = request.FILES.get('image')
        if form.is_valid():
            new_video_info = form.save(commit=False)
            new_video_info.video_img = upload_image
            new_video_info.save()
            return HttpResponse('1')
        else:
            return HttpResponse('error')
    else:
        form = Video_infoForm()
        context = {}
        context['form'] = form
        return render(request , 'account/create_video_info.html' , context) 

