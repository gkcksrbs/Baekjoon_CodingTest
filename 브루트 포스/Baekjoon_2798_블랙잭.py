
while(True):
    N, M = map(int, input().split())

    if(3<= N <= 100 and 10 <= M<= 300000):
        break

while(True):
    input_lst = list(map(int, input().split()))

    if(len(input_lst) == N):
        break

sum_lst = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_lst.append(input_lst[i]+input_lst[j]+input_lst[k])

sum_lst = sorted(sum_lst)

while(True):
    if (sum_lst[len(sum_lst) - 1] > M):
        sum_lst.pop()
    else:
        print(sum_lst.pop())
        break
