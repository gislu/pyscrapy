# -*- coding: utf-8 -*-  
#---------------------------------------  
#   program：爬虫1.0   
#   author：GisLu
#   data：2014-04-02  
#---------------------------------------

import urllib
import urllib2
import cookielib
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8') 


def catch():
# 102 三里街子站    103 长江中路    104  琥珀山庄   105 明珠广场   106  董铺水库
#107  庐阳区子站  108 瑶海区子站 109 包河区子站 110滨湖新区子站 111高新区子站 112全市总体
    city=re.compile(r'KQGrid1_ctl02_lblCity"><span id=(.*?) onclick')
    num=re.compile(r'ctl02_lblAPI">(.*?)</span>')
    level=re.compile(r'Krid1_ctl02_lblLevel">(.*?)</span>')
    condition=re.compile(r'_ctl02_lblCondition">(.*?)</span>')
    panorama=re.compile(r'KQGrid1_ctl02_lblCity"><span id=(.*?) onclick[\d\D]*?KQGrid1_ctl02_lblAPI">(.*?)</span>[\d\D]*?KQGrid1_ctl02_lblLevel">(.*?)</span>[\d\D]*?KQGrid1_ctl02_lblCondition">(.*?)</span>')
    for i in panorama.finditer(str1):    
        print i.group(1)
        print i.group(2)
        print i.group(3).decode('utf-8')
        print i.group(4).decode('utf-8')


 

def data():
    data=re.compile(r'border-right: 1px #CCE4CA solid;">([\d\D]*?)</td>')
    for i in data.finditer(str1):
        a=i.group(1).decode('utf-8').strip()
        b=a.strip('&nbsp;')+'\n'
        
        c.write(b)

        
if __name__ == "__main__":
    cj=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
    headers={
        'Host':'www.hfepb.gov.cn'
        }
    url1="http://www.hfepb.gov.cn/Showair.aspx?page="
    path=str("D:/record.txt")
    c=open(path,"w+")  
    #!!日期
    for i in range(1,1398):
        url=url1+str(i)  
        req=urllib2.Request(url)
        event=urllib2.urlopen(req)
        str1=event.read()
        data()
        c.close  


