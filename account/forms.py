from video.models import *
from django import forms

class Video_infoForm(forms.ModelForm):
    class Meta:
        model = Video_info
        fields = ('video_type' , 'video_title' , 'video_detail')
        widgets = {
            "video_type":forms.Select(attrs={'class':'form-control'}),
            "video_title":forms.TextInput(attrs={'class':'form-control'}),
            "video_detail":forms.Textarea(attrs={'class':'form-control'}),
        }