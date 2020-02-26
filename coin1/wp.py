import socket

r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect(('pwnable.kr', 9007))

print r.recv(2048)
#r.recvuntil("Ready? starting in 3 sec... -\n\n\n")

def solve():
    data = r.recv(1024)
    print 'data:' + data
    N = int(data.split(' ')[0].split('=')[1])
    C = int(data.split(' ')[1].split('=')[1])
    
    L, R, t, Times = 0, N - 1, 0, C
    while t <= Times:
        t = t + 1
        if L == R:
            r.send(str(L) + '\n')
            data = r.recv(32)
            print 'send:' + str(L)
            print 'data:' + data
        else:
            mid = (L + R) / 2
            p = ' '.join(str(i) for i in range(L, mid + 1))
            print "send:" + p
            r.send(p + '\n')
            data = r.recv(32)
            print 'data:' + data
            if int(data) % 10 == 0:
                L = mid + 1
            else:
                R = mid

for i in range(100):
    solve()

print r.recv(1024)
