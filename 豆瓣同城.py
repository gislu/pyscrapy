# -*- coding: utf-8 -*-  
#---------------------------------------  
#   program：豆瓣同城爬虫   
#   author：GisLu
#   data：2014-02-08  
#---------------------------------------

import urllib
import urllib2
import cookielib
import re

cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#内容提取   
def search(str1):
    regex=re.compile(r'summary">([\d\D]*?)</span>[\d\D]*?class="hidden-xs">([\d\D]*?)<time[\d\D]*?<li title="([\d\D]*?)">[\d\D]*?strong>([\d\D]*?)</strong>')
    for i in regex.finditer(str1):
        print "活动地点",i.group(1)
        a=i.group(2)
        b=a.replace('</span>','')
        print b.replace('\n','')
        print i.group(3)
        c=i.group(4).decode('utf-8')
        print c,'\n'
 

#获取url
for i in range(0,5):
    url="http://beijing.douban.com/events/future-all?start="
    url=url+str(i*10)
    req=urllib2.Request(url)
    event=urllib2.urlopen(req)
    str1=event.read()
    search(str1)




