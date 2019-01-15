# _*_ code:utf-8 _*_
#!/usr/local/bin/python

import socket

s = socket.socket()
s.connect(('127.0.0.1', 8000))
msg = input("Please input your message:")
s.sendall(bytearray(msg,encoding="utf-8"))
print(str(s.recv(1024),encoding='utf-8'))
s.close()