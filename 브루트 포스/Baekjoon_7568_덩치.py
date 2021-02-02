while(True):
    N = int((input()))

    if(2 <= N <= 50):
        break

lst = []
for i in range(N):
    while(True):
        x,y = map(int, input().split())

        if(10 <= x , y <= 200):
            lst.append([x, y])
            break

rank_lst = ""
for i in lst:
    rank = 1
    for j in lst:
        if(i[0] < j[0] and i[1] < j[1]):
            rank += 1
    rank_lst = rank_lst + str(rank) + " "

print(rank_lst)