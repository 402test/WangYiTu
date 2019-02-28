from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name='昵称',default='')
    birday = models.DateField(verbose_name='生日',null=True,blank=True)
    gender = models.CharField(max_length=6,choices=(('male','男'),('female','女')),default="female")
    image = models.ImageField(upload_to='imgage/%Y/%m',default='image/defalt.jpg',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username



class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    send_type = models.CharField(max_length=10,choices=(('register','注册'),('forget','找回密码')))



