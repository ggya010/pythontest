import httplib
import threading,time
params = 'TIM:UTC 2016-03-23 03:23:14,PTY:G6S,VER:V1.1.4-US;V2.30,NAM:G6S,SPT:24H,CID:89860021191586059282'
headers = {"Content-type": "application/x-www-form-urlencoded" , "Connection": "Keep-Alive"}

oknum = 0
o200num = 0
def gicusTestThread(interval):
    httpClient = None
    i = 0
    global oknum
    global o200num
    while i<1:
#        print('now is %s times' % i)
        a = time.clock()
        httpclient = httplib.HTTPConnection('gicus.gosafesystems.com',8080,timeout=30)
        httpclient.request('POST','/Dev.php?mei=351535058559550',body=params,headers=headers)
        response = httpclient.getresponse()
        if response.status == 200:
            o200num += 1
        if response.reason == 'OK':
            oknum += 1
        print(response.status)
        print(time.clock()-a)
        # print('-----------------')
        # print(response.reason)
        # print(response.read())
        time.sleep(interval)
        i += 1

n = 0
pool = []
while n<1:
    pool.append(threading.Thread(target=gicusTestThread,args=(1,)))
    pool[-1].start()
    n += 1
for i in pool:
    i.join()
print('the http ok is %s, 200 is %s ' % (oknum, o200num))


