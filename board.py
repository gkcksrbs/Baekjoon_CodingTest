import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

tmp = list(set(lst))
tmp.sort()
tmp = {tmp[i]: i for i in range(len(tmp))}

print(*[tmp[i] for i in lst])