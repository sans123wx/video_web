from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ['title' , 'content' , 'image']