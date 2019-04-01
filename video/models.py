from django.db import models

# Create your models here.
#图片上传保存路径
def up_to_img(instance , filename):
    return 'video/%s/%s/img/%s'%(instance.video_type.title , instance.video_title , filename)

#视频上传保存路径
def up_to_video(instance , filename):
    return 'video/%s/%s/video/%s'%(instance.title.video_type.title , instance.title.video_title , filename)

#视频分类
class Video_type(models.Model):
    title = models.CharField(max_length = 50 , verbose_name = '视频分类')
    def __str__(self):
        return self.title

#视频信息
class Video_info(models.Model):
    video_type = models.ForeignKey(Video_type , on_delete = models.DO_NOTHING , verbose_name = '视频分类')
    video_title = models.CharField(max_length = 50 , verbose_name = '视频名称')
    video_detail = models.TextField(verbose_name = '视频内容简述')
    video_img = models.ImageField(upload_to = up_to_img , verbose_name = '图片')
    def __str__(self):
        return self.video_title

#视频
class Video(models.Model):
    title = models.ForeignKey(Video_info , on_delete = models.DO_NOTHING , verbose_name = '视频名称')
    video = models.FileField(upload_to = up_to_video , verbose_name = '视频')
    def __str__(self):
        return self.title.video_title