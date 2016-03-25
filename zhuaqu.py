import urllib2
import re
def catchall(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
    except urllib2.URLError,e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
    return response.read().decode('utf-8')

def getmessage(content):
    pattern = re.compile('<div class="content">(.*?)<.*?</div>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print(item)

page = 2
url = 'http://www.qiushibaike.com/hot/page/'+str(page)
a = catchall(url)
getmessage(a)
