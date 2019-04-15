from video.models import *
from django import forms

class Video_infoForm(forms.ModelForm):
    class Meta:
        model = Video_info
        fields = ('video_type' , 'video_title' , 'video_detail')