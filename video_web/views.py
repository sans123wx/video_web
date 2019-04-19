from video.models import *
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.db.models import Q

@require_POST
def search(request):
    wd = request.POST.get('wd').strip()
    if wd:
        con = Q()
        for word in wd.split(' '):
            con = con | Q(video_title__icontains = word)
        result = Video_info.objects.filter(con)
    else:
        result = Video_info.objects.none()
    context = {}
    context['result'] = result
    context['wd'] = wd
    return render(request , 'video/result.html' , context)
