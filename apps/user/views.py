from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# Create your views here.


from .form import LoginForm,RegisterForm,ForgetForm
from user.models import UserProfile,EmailVerifyRecord
from .tool.tool_send_email import send_register_email


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
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('index'))
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



class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))

class ForgetPwdView(View):
    '''
    忘记密码的傻孩子来了
    '''
    def get(self,request):
        forgetform = ForgetForm()   #  验证码
        return render(request,'forget.html',{'forgetform':forgetform})

    def post(self,request):
        forgetform = ForgetForm(request.POST )
        if forgetform.is_valid():
            email = request.POST.get('email')
            #  判断该邮箱是否注册
            user = UserProfile.objects.get(email=email)
            if not user:
                return render(request, 'forget.html', {'msg': 'not_register', 'forgetform': forgetform})
            email_res = send_register_email(email,'forget')
            if not email_res:
                return render(request, 'forget.html', {'msg': 'error', 'forgetform': forgetform})
            #  修改user 的 updatapassword
            user.updata_pwd = make_password(request.POST.get('password'))
            user.save()
            return render(request,'forget.html',{'msg':'true', 'forgetform': forgetform})

        else:
            return render(request, 'forget.html', {'forgetform': forgetform})




class Active_User_View(View):
    def get(self,request,active_code):
            code_model = EmailVerifyRecord.objects.get(code=active_code)
            if not code_model:
                return render(request,'active_error.html')
            user = UserProfile.objects.get(email=code_model.email)
            if code_model.send_type =='register':
                # 注册激活 验证码
                user.is_active = True
                user.save()
                return HttpResponse('激活成功')
            elif code_model.send_type =='forget':
                user.password = user.updata_pwd
                user.save()
                return HttpResponse('修改成功')


class Active_Pwd_View(View):
    pass