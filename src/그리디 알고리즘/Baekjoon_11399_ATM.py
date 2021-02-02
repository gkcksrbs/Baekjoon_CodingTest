import sys

N = int(sys.stdin.readline())
lst = list(map(int, input().split()))

lst.sort()

time = [0]*N

for i in range(N):
    tmp = 0
    for j in range(i+1):
        tmp += lst[j]
    time[i] = tmp

print(sum(time))
