from django.db import models
# Create your models here.

from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    updata_pwd = models.CharField(max_length=200,verbose_name='更新暂存密码',default='' ,null=True,blank=True)
    nick_name = models.CharField(max_length=50,verbose_name='昵称',default='默认昵称')
    birday = models.DateField(verbose_name='生日',null=True,blank=True)
    gender = models.CharField(max_length=6,choices=(('male','男'),('female','女')),default="female")
    image = models.ImageField(upload_to='image/%Y/%m',default='image/defalt.jpg',max_length=100)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username



class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    send_type = models.CharField(max_length=10,choices=(('register','注册'),('forget','找回密码')))

    def __str__(self):
        return '验证码:%s'%self.code

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural  = verbose_name
# class Collection_M(models.Model):
#
#     user = models.ForeignKey(UserProfile,verbose_name='用户', on_delete=models.CASCADE)
#     multi = models.ForeignKey(Multi_M, verbose_name='媒体文件', on_delete=models.CASCADE)
#     open = models.CharField(max_length=10,choices=(('t','公布'),('f','不公布')))
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
#
#     class Meta:
#         verbose_name = '用户收藏'
#         verbose_name_plural = verbose_name
