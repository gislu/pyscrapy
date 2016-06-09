import urllib
#---------------------------------------  
#   @program：图书借阅查询   
#   @author：GisLu
#   @data：2014-02-08  
#---------------------------------------

import urllib2
import cookielib
import re

cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]

urllib2.install_opener(opener)

#登陆获取cookies
postdata=urllib.urlencode({
        'user':'X21114044',
        'pw':'121110',
        'imageField.x':'0',
        'imageField.y':'0'})


    
rep=urllib2.Request(
           url='http://210.45.210.6/dzjs/login.asp',
           data=postdata
        )
result=urllib2.urlopen(rep)
print result.geturl()



#获取账目表

Postdata=urllib.urlencode({
        'nCxfs':'1',
        'submit1':'检索'})

aa=urllib2.Request(
    url='http://210.45.210.6/dzjs/jhcx.asp',
    data=Postdata
    )
bb=urllib2.urlopen(aa)
cc=bb.read()
print cc
zhangmu=re.findall('tdborder4  >(.*?)</td>',cc)

for i in zhangmu:
    i=i.decode('gb2312')
    i=i.encode('gb2312')
    print i.strip('&nbsp;')




