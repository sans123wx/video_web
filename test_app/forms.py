from django import forms
from .models import *

class TestModelForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ('title' , 'content')