import sys

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    check = [0]*N
    check[M] = 1
    count = 0
    while True:
        if lst[0] == max(lst):
            count += 1
            if(check[0] == 1):
                print(count)
                break
            else:
                lst.pop(0)
                check.pop(0)
        else:
            lst.append(lst.pop(0))
            check.append(check.pop(0))



