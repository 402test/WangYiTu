import random
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.core.paginator import Paginator
# Create your views here.
from django.views.generic.base import View
from multi.models import Multi_M
from utils.mixin_utils import LoginRequiredMixin
from spider.search import Index_Spider
class IndexView(View):
    '''
    主页   每日推荐
    '''
    def get(self,request):

        x = random.randint(1,500)
        print(x)
        multi = Multi_M.objects.all()[x:x+20]
        return render(request,'index.html',{'multis':multi})



class TypedataView(View):
    def get(self,request):
        type = request.GET.get('type')
        musics = Multi_M.objects.filter(music_type=type)
        p = Paginator(musics, 20)
        L_music = []
        id = request.GET.get('id',1)
        for i in p.page(int(id)):
            L_music.append([i.multi_name,i.multi_s,i.nums,i.id,i.multi_src])
        return HttpResponse(json.dumps({'data':L_music,'nums':p.num_pages,'type':type}), content_type='application/json')


class SearchView(View):
    def get(self,request):
        key = request.GET.get('key')
        sp = Index_Spider(key)
        data = sp.run()
        return HttpResponse(data,content_type='application/json')



class MusicView(View):
    def get(self,request,music_id):
        music = Multi_M.objects.get(id=music_id)

        return render(request,'music.html',{'music':music})


