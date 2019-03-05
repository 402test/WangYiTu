from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# Create your views here.


from .form import LoginForm,RegisterForm
from user.models import UserProfile
from tool.tool_send_email import send_register_email


# 重写登陆验证机制   实现用户名  邮箱都可以登陆
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    '''
    登陆模块
    '''

    def get(self, request):
        login_form = LoginForm()    #  form  里面有验证码  传递到前端
        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        if login_form.is_valid():
            # 用户名 邮箱 都要能登陆 所以重写一下  authenticate
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                   login(request,user)
                   return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, "login.html", {"msg": "用户未激活！", 'login_form': login_form})
            else:
                return render(request, "login.html", {"msg": "用户或密码错误！", 'login_form': login_form})
        else:
            #  格式错误
            return render(request, 'login.html', {'login_form': login_form})


class IndexView(View):
    '''
    主页
    '''
    def get(self,request):
        return render(request,'index.html')

class RegisterView(View):
    '''
    注册
    '''
    def get(self,request):
        regiter_form = RegisterForm()
        return render(request,'register.html',{'regiter_form':regiter_form})

    def post(self,request):
        regiter_form = RegisterForm(request.POST)
        if regiter_form.is_valid():
            user_name = request.POST.get('email','')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'msg': 'already','regiter_form':regiter_form})

            #  发送邮件
            email_res  = send_register_email(user_name)
            if not email_res:
                return render(request, 'register.html', {'msg': 'error', 'regiter_form': regiter_form})
            #  保存到数据库
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()


            return render(request, "register.html",{'msg':'true' ,'regiter_form':regiter_form})
        else:
            return render(request,'register.html',{'regiter_form':regiter_form})
