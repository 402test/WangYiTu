"""Wa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from multi.views import IndexView,TypedataView,SearchView,MusicView
from collection.views import CollectionView
from user.views import LoginView,RegisterView,LogoutView,ForgetPwdView,Active_User_View,InfoView,ImageUpdate
from Wa.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    url(r'^forget/$',ForgetPwdView.as_view(),name='forget'),
    url(r'^active/(?P<active_code>.*)/$', Active_User_View.as_view(), name="user_active"),
    url(r'^type/$',TypedataView.as_view(), name='type'),
    url(r'^collection/$',CollectionView.as_view(), name='collection'),
    url(r'^search/$',SearchView.as_view(),name='search'),
    url(r'^user_info/$',InfoView.as_view(),name = 'info'),
    url(r'^image_update/$',ImageUpdate.as_view(),name = 'image_update'),
    url(r'^music/(?P<music_id>.*)/$',MusicView.as_view(),name='music'),
]
