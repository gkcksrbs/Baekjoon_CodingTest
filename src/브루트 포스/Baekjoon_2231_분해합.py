while(True):
    Num = int(input())

    if(1 <= Num <= 1000000):
        break

for i in range(Num+1):
    lst = list(map(int, str(i)))
    Sum = i + sum(lst)

    if(Sum== Num):
        print(i)
        break
    if(i == Num):
        print(0)
        break