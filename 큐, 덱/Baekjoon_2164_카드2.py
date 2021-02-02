import sys
from _collections import deque

N = int(sys.stdin.readline())
D = deque()

for i in range(N):
    D.append(i+1)

while D.__len__() != 1:
    D.popleft()

    if D.__len__() == 1:
        break

    D.append(D.popleft())

print(D.pop())