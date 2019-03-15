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
            user = request.user
            id = request.GET.get('id')
            music =Multi_M.objects.filter(id=id).first()
            collection = Collection_M()
            collection.user = user
            collection.multi = music
            collection.save()   #  在Collection_M 里面 重写了save  让  歌曲收藏 加 1
            data = '收藏成功'

        else:
            data = '请先登录'
        return HttpResponse(json.dumps({'data':'%s'%(data)}),content_type='application/json')