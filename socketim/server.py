# _*_ code:utf-8 _*_
#!/usr/local/bin/python

import socket

s = socket.socket()
# 建立绑定ip和端口
s.bind(('127.0.0.1',8000))
# 监听连接请求
s.listen(2)
print('start listening ...')
# 循环监听client发来的消息
while 1:
    # 获取链接IP和端口
    conn, addr = s.accept()
    print('['+addr[0]+':'+str(addr[1])+'] send a message to me: '+conn.recv(1024))
    conn.sendall('I received a message from ['+addr[0]+':'+str(addr[1])+']')
s.close()
