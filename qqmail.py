import os
import re
import time
import email
import poplib
import time
from email.parser import Parser
import re
import imaplib
import cStringIO
from hashlib import md5
tt1 = time.clock()
def gethotmailsub(conn,num,sub):
    hotlist = []
    emailmsgnum, emailsize = conn.stat()
    for i in range(emailmsgnum-num, emailmsgnum+1):
        c = conn.retr(i)[1]
        dd = iter(c)
        while True:
            try:
                if next(dd) == sub:
                    hotlist.append(i)
                    break
            except StopIteration:
                break
        # if sub in c:
        #     hotlist.append(i)
    return hotlist
class hotmail:
    def __init__(self):
        self.b = 'Subject: HotForex PAMM Daily Report'
        self.mymm = []
    def getmymm(self, conn, num, keyword):
        self.num = num
        self.keyword = keyword
        self.conn = conn
        c = self.conn.retr(self.num)[1]
        itc = iter(c)
        while True:
            try:
                nc = next(itc)
                if self.keyword in nc:
                    self.mymm.append(nc)
            except StopIteration:
                break
#        print(self.num)
#         for i in c:
#             if self.keyword in i:
#                 self.mymm.append(i)
        return self.mymm[1]
MAILADDR = "@qq.com"
PASSWORD = ""
SERVER = "pop.qq.com"
PROTOCOL = "pop3"
USE_SSL = True
OUTDIR = "result"
# Connect to mail server
conn = poplib.POP3_SSL('pop.qq.com', 995)
conn.user(MAILADDR)
conn.pass_(PASSWORD)

print("[+] Connect to {0}:{1} successfully".format('pop.qq.com', 995))
emailmsgnum, emailsize = conn.stat()
print 'email number is %d and size is %d'%(emailmsgnum, emailsize)
hostlist = gethotmailsub(conn, 51,'Subject: HotForex PAMM Daily Report')
print hostlist
for i in hostlist:
    s = hotmail()
    x = s.getmymm(conn, i, 'My Equity: ')
    print(x)

conn.quit()
tt2 = time.clock()
print(tt2-tt1)
