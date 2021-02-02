N = int(input())
lst = []

for i in range(N):
    Num = int(input())

    if Num == 0:
        lst.pop()
    else:
        lst.append(Num)

print(sum(lst))