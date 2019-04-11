from django.db import models

# Create your models here.

def upload_to_img(instance , filename):
    return 'test/%s/%s.jpeg'%(instance.title , filename)

class TestModel(models.Model):
    title = models.CharField(max_length = 50 , verbose_name = '测试标题')
    content = models.TextField(verbose_name = '测试内容')
    image = models.ImageField(upload_to = upload_to_img , verbose_name = '图片')