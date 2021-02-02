N, M = map(int, input().split())

num_lst = [1+i for i in range(N)]
check_num = [False for i in range(N)]
lst = []

def recur(index):
    if index == M:
        for i in lst:
            print(i, end=' ')
        print()
        return

    for i in range(N):
        if check_num[i]:
            continue

        lst.append(num_lst[i])
        check_num[i] = True

        recur(index+1)

        lst.pop()
        check_num[i] = False

recur(0)

