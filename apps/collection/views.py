import json

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.generic.base import View
from multi.models import Multi_M
from collection.models import Collection_M
class CollectionView(View):
    def get(self,request):
        if request.user.is_authenticated():

            if  request.GET.get('name'):
                #  没有的话  可能是用户收藏了 搜索出来的音乐
                #  这个时候  要先添加进数据库  再 收藏
                music = Multi_M()
                music.multi_name = request.GET.get('name')
                music.multi_s = request.GET.get('singer')
                music.nums = 0
                music.music_type = 'Recommend'
                music.multi_src = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(request.GET.get('id'))
                music.save()
            else:
                id = request.GET.get('id')
                music = Multi_M.objects.filter(id=id).first()
            user = request.user
            collection = Collection_M()
            if Collection_M.objects.filter(user=user,multi=music):
                 data = '已经收藏过啦'
            else:
                collection.user = user
                collection.multi = music
                collection.save()   #  在Collection_M 里面 重写了save  让  歌曲收藏 加 1
                data = '收藏成功'

        else:
            data = '请先登录'
        return HttpResponse(json.dumps({'data':'%s'%(data)}),content_type='application/json')