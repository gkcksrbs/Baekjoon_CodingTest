import re
import sys
from _collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    Str = sys.stdin.readline()
    p = p.replace('RR', '')
    lst = re.findall("\d+", Str)
    D = deque()
    Check = True
    r = 0

    for j in lst:
        D.append(int(j))

    for k in p:
        if k =='R':
            r += 1

        elif k =='D':
            if D.__len__() == 0:
                Check = False
                break
            else:
                if r % 2 == 0:
                    D.popleft()
                else:
                    D.pop()

    if not Check:
        print('error')
    else:
        if r % 2 == 0:
            pass
        else:
            D.reverse()

        print("[", end='')
        for i in range(len(D)):
            if i == len(D) - 1:
                print(D[i], end='')
            else:
                print("%s," % (D[i]), end='')
        print("]")
