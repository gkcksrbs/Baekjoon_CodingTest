N = int(input())

lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))


lst.sort(key=lambda x:(x[1], x[0]))


start_time = 0
count = 0
for i in range(len(lst)):
    if start_time <= lst[i][0]:
        start_time = lst[i][1]
        count += 1

print(count)