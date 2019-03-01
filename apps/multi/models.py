from datetime import datetime

from django.db import models

from user.models import UserProfile
# Create your models here.

class Multi_M(models.Model):

    '''
    主页歌曲
    '''
    multi_name = models.CharField(max_length=50,verbose_name='歌名')
    multi_src  = models.CharField(max_length=150,verbose_name='链接')
    multi_s = models.CharField(max_length=10,verbose_name='歌手')
    nums = models.IntegerField(default=0,verbose_name='收藏数')
    music_type =models.CharField(max_length=20, verbose_name='音乐类型',choices=(('popular','流行'),('Recommend','站长推荐'),('cure','治愈'),('rock','摇滚'),('Light_music','轻音乐')))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    image = models.ImageField(upload_to='imgage/%Y/%m', default='image/music.jpg', max_length=100)

    class Meta:
        verbose_name = '主页歌曲'
        verbose_name_plural = verbose_name




#  评论    两个外键   待完善

class Comment(models.Model):
    multi = models.ForeignKey(Multi_M,verbose_name='媒体文件',on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    txt = models.CharField(max_length=200,verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name