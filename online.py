import httplib, binascii
import time  
import thread 

def gicusTestThread(no,interval):
    cnt = 0
    while cnt < 500:
        print 'Thread:(%d) Time:%s\n' % (no, time.ctime())
        httpClient = None
        params = 'TIM:UTC 2016-03-23 03:23:14,PTY:G6S,VER:V1.1.4-US;V2.30,NAM:G6S,SPT:24H,CID:89860021191586059282'
        headers = {"Content-type": "application/x-www-form-urlencoded" , "Connection": "Keep-Alive"}
        httpClient = httplib.HTTPConnection('gicus.gosafesystems.com',8080,timeout = 30)
        httpClient.request('POST','/Dev.php?mei=351535058559550',body=params,headers=headers)
        response = httpClient.getresponse()
        print(response.status)
        print(response.reason)
        print(response.read())
        httpClient.close()
        time.sleep(interval)
        cnt += 1
    thread.exit_thread()


def gicusTest():
    thread_cnt = 1
    while thread_cnt < 5:
        thread.start_new_thread(gicusTestThread,(thread_cnt,10))
        thread_cnt += 1

if __name__ == '__main__':
    gicusTest()
