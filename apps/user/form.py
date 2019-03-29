# encoding: utf-8
__author__ = 'ChengweiHuang'
__date__ = '2019/3/4 17:28'
import re
from django import forms

from captcha.fields import CaptchaField
from user.models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=6)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class UpdateInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name','gender','username']

    def clean_username(self):
            username = self.cleaned_data['username']
            username_regex = '[a-zA-Z0-9_-]{6,24}'
            if re.search(username_regex,username):
                return username
            else:

                raise forms.ValidationError('用户名不规范 应使用长度为6-24的数字字母下划线', code='invalid username')



class ImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = ['image']