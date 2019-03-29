# encoding: utf-8
'''

独立的爬虫py  跟框架没有联系   改变 url  下载不同的 歌单分类里面的音乐
'''

__author__ = 'ChengweiHuang'
__date__ = '2019/3/11 9:37'
import requests
from bs4 import BeautifulSoup
import re
import json
import pymysql
from datetime import datetime
db = pymysql.connect("localhost","root","123456","Wa_mysql" )

cursor = db.cursor()

LINK_DOWN = 'http://music.163.com/song/media/outer/url?id=%s.mp3'    #   下载链接 添加歌曲id
LINK_MESS = 'http://music.163.com/api/song/detail/?id={}&ids=%5B{}%5D'
type = 'cure'

url = 'https://music.163.com/playlist?id=447397102'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
    'Host':'music.163.com',
    'Referer':'https://www.baidu.com/link?url=ZSrB3llqBVzeT3jkByKzLl4_XTI7mcwuCaG3aTq1GQG&wd=&eqid=ecaff99f000680a1000000055c85bf51',
}

headers_link = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',

}
res = requests.get(url=url,headers = headers).content
soup = BeautifulSoup(res,'html.parser')
sql = 'insert into multi_multi_m(multi_name,multi_src,multi_s,music_type,image,add_time,nums) values (%s,%s,%s,%s,%s,%s,%s)'
for i in soup.select('.f-hide li a'):
    id = re.findall(r'\d+',i['href'])[0]
    link = LINK_DOWN%id
    res_json = requests.get(url=LINK_MESS.format(id,id),headers = headers_link)
    res_json = json.loads(res_json.content)
    j =res_json['songs'][0]
    singer = j['artists'][0]['name']
    img_url = j['artists'][0]['picUrl']
    #  下载图片
    f_src = id+'ofimg.jpg'
    f_data = requests.get(url=img_url,headers=headers_link).content
    with open('../../../media/image/'+f_src,'wb') as f:
        f.write(f_data)
    cursor.execute(sql,[i.text,link,singer,type,f_src,datetime.now(),0])
    db.commit()

