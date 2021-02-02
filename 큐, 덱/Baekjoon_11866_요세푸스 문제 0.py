import sys
from _collections import deque

N, K = map(int, sys.stdin.readline().split())
D = deque()
Str = "<"

for i in range(N):
    D.append(i+1)

for i in range(N):
    for j in range(K-1):
        D.append(D.popleft())

    if i != N-1:
        Str = Str + str(D.popleft()) + ", "
    else:
        Str = Str + str(D.popleft()) + ">"

print(Str)