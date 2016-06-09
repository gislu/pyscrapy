import urllib
import urllib2
import cookielib

cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]

urllib2.install_opener(opener)

#登陆获取cookies
postdata=urllib.urlencode({
        '__VIEWSTATE':'/wEPDwUKMTg5NjY5MDM3OWRkRepo7pgO2y5BnwW7HGaJWwNW1Mk=',
        'TextBox1':'X21114044',
        'TextBox2':'ahlxt12',
        'ddl_js':'学生',
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
result=urllib2.urlopen(rep)
print result.getcode() 

