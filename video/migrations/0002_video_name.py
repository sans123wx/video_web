# Generated by Django 2.1.7 on 2019-04-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default='无', max_length=50),
        ),
    ]