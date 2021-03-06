# Generated by Django 2.1.7 on 2019-04-01 07:57

from django.db import migrations, models
import django.db.models.deletion
import video.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=video.models.up_to_video, verbose_name='视频')),
            ],
        ),
        migrations.CreateModel(
            name='Video_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=50, verbose_name='视频名称')),
                ('video_detail', models.TextField(verbose_name='视频内容简述')),
                ('video_img', models.ImageField(upload_to=video.models.up_to_img, verbose_name='图片')),
            ],
        ),
        migrations.CreateModel(
            name='Video_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='视频分类')),
            ],
        ),
        migrations.AddField(
            model_name='video_info',
            name='video_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='video.Video_type', verbose_name='视频分类'),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='video.Video_info', verbose_name='视频名称'),
        ),
    ]
