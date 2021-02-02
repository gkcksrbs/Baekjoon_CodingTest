N, M = map(int, input().split())

num_lst = [1+i for i in range(N)]
lst = []
check_num = [False for i in range(N)]

def recur(index, next):
    if index == M:
        for i in lst:
            print(i, end=' ')
        print()
        return

    for i in range(next, N):
        if check_num[i]:
            continue

        check_num[i] = True
        lst.append(num_lst[i])


        recur(index+1, i+1)

        lst.pop()
        check_num[i] = False

recur(0, 0)
