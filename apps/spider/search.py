# encoding: utf-8
__author__ = 'ChengweiHuang'
__date__ = '2019/3/14 15:54'
import requests
import json
'''
搜索歌曲爬虫   然后 被主页的搜索框调用啊
  接口来源 https://www.jianshu.com/p/1bbdd16b1726
  网速不够 怎么解决！！  
'''

class Index_Spider(object):
    headers = {
        'Host':'music.163.com',
      'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
    }

    def __init__(self,data,nums = 50):
        '''

        :param data:  被搜索的关键字
        '''
        self.data = data
        self.nums = nums
        #   url  接受  歌曲名称  和搜索条数两个参数
        self.url = 'http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={}&type=1&offset=0&total=true&limit={}'.format(data,nums)

    def run(self):
        html = requests.get(url=self.url,headers = self.headers).content
        return html


if __name__ =='__main__':
    sp = Index_Spider('许嵩')
    sp.run()