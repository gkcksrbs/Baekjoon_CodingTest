import sys
from _collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
D = deque()
count = 0

for i in range(N):
    D.append(i+1)

lst = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(lst.__len__()):
    if D.index(lst[i]) == 0:
        D.popleft()
    else:
        index = D.index(lst[i])
        if index < D.__len__() - index + 1:
            for j in range(index):
                D.append(D.popleft())
                count += 1
        else:
            for j in range(D.__len__() - index):
                D.appendleft(D.pop())
                count += 1
        D.popleft()

print(count)
