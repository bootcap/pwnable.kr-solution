from pwn import *
import socket

arg = ['a' for i in range(100)]
arg[ord('A')] = '\x00'
arg[ord('B')] = '\x20\x0a\x0d'
_port = 1234
arg[ord('C')] = str(_port)


in_std = open('/tmp/1.txt', 'w')
in_std.write('\x00\x0a\x00\xff')
in_std.close()
in_stderr = open('/tmp/2.txt', 'w')
in_stderr.write('\x00\x0a\x02\xff')
in_stderr.close()
in_file = open('./\x0a', 'w')
in_file.write('\x00\x00\x00\x00')
in_file.close()

in_std = open('/tmp/1.txt', 'r')
in_stderr = open('/tmp/2.txt', 'r')
in_env = {'\xde\xad\xbe\xef':'\xca\xfe\xba\xbe'}

###### run
r = process(executable = './input', argv = arg, stdin = in_std, stderr = in_stderr, env = in_env)

print r.recvuntil('Stage 1 clear!\n')
print r.recvuntil('Stage 2 clear!\n')
print r.recvuntil('Stage 3 clear!\n')
print r.recvuntil('Stage 4 clear!\n')

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.connect(('127.0.0.1', _port))
skt.send('\xde\xad\xbe\xef')
skt.close()

print r.recvuntil('Stage 5 clear!\n')
print r.recv()

r.close()
