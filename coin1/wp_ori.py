from pwn import *

r = remote("pwnable.kr", "9007")

print r.recv(timeout=2900)
#r.recvuntil("Ready? starting in 3 sec... -\n\n\n")

def solve():
    data = r.recv(timeout=200)
    print 'data:' + data
    N = int(data.split(' ')[0].split('=')[1])
    C = int(data.split(' ')[1].split('=')[1])
    
    L, R, t, Times = 0, N - 1, 0, C
    while t <= Times:
        t = t + 1
        if L == R:
            r.sendline(str(L))
            data = r.recv()
            print 'send:' + str(L)
            print 'data:' + data
        else:
            mid = (L + R) / 2
            p = ' '.join(str(i) for i in range(L, mid + 1))
            print "send:" + p
            r.sendline(p)
            data = r.recv()
            print 'data:' + data
            if int(data) % 10 == 0:
                L = mid + 1
            else:
                R = mid

for i in range(100):
    solve()

print r.recv()
