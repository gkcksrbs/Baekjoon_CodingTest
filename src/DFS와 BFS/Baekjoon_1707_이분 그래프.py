import sys
from _collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    result = True
    v, e = map(int, input().split())
    data = [[]for _ in range(v+1)]
    visited = [-1] * (v+1)
    for _ in range(e):
        n1, n2 = map(int, input().split())
        data[n1].append(n2)
        data[n2].append(n1)
    q = deque()
    visited[1] = 0
    q.append(1)
    while q:
        now = q.popleft()
        for n in data[now]:
            if visited[n] != -1:
                if visited[n] == visited[now]:
                    result = False
            else:
                if visited[now] == 0:
                    visited[n] = 1
                else:
                    visited[n] = 0
                q.append(n)
    for i in range(1, v+1):
        if visited[i] == -1:
            result = False
    if result:
        print('YES')
    else:
        print('NO')