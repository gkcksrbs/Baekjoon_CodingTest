N = int(input())

lst = [[] for i in range(201)]

for i in range(N):
    member = list(map(str, input().split()))

    lst[int(member[0])].append(member[1])

for i in range(201):
    if(lst[i] != None):
        for j in lst[i]:
            print(str(i) + " " + j)



