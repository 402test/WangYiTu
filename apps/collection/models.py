from datetime import datetime

from django.db import models
from multi.models import Multi_M
from user.models import UserProfile
# Create your models here.


class Collection_M(models.Model):

    user = models.ForeignKey(UserProfile,verbose_name='用户', on_delete=models.CASCADE)
    multi = models.ForeignKey(Multi_M, verbose_name='媒体文件', on_delete=models.CASCADE)
    open = models.CharField(max_length=10,choices=(('t','公布'),('f','不公布')),default='f')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

       #  每次添加数据的时候啊  就要把歌曲的 收藏数 这个属性加1

        self.multi.nums+=1
        self.multi.save()
        super(Collection_M,self).save(force_insert,force_update,using,update_fields)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

