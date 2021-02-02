N, M = map(int, input().split())

Num = [i+1 for i in range(N)]
lst = [0 for i in range(M)]
check_num = [False for i in range(N)]
def recur(index):
    if(index == M):
        for i in lst:
            print(i, end=' ')
        print()
        return

    for i in range( N):
        if check_num[i]:
            continue

        lst[index] = Num[i]
        recur(index+1)
        check_num[i] = True
        
        for j in range(i+1, N):
            check_num[j] = False

recur(0)