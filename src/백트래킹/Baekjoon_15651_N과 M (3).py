N, M = map(int, input().split())

Num = [i+1 for i in range(N)]
lst = [0 for i in range(M)]

def recur(index):
    if(index == M):
        for i in lst:
            print(i, end=' ')
        print()
        return

    for i in range(N):
        lst[index] = Num[i]
        recur(index+1)


recur(0)