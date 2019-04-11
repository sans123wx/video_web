from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.

def test(request):
    if request.method == "POST":
        form = TestModelForm(request.POST)
        if form.is_valid():
            print(2)
            new_test = form.save(commit=False)
            new_test.image = request.FILES.get('image')
            new_test.save()
            return HttpResponse('1')
    else:
        form = TestModelForm()
        return render(request , 'test/test.html' , {'form':form})

def result(request):
    img = TestModel.objects.last()
    context = {}
    context['img'] = img
    return render(request , 'test/test2.html' , context)
