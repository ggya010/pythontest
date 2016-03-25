import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
name = 'test1: '
while True:
    print(s.recv(1024).decode('utf-8'))
    a = raw_input()
    if a == 'exit':
        break
    a = name + a
    print(a)
    s.send(a)
s.close()