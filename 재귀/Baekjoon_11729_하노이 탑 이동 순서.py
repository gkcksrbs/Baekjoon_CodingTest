def Hanoi(n, From, to, other):
    if (n == 1):
        print(str(From) +" "+ str(to))
    else:
        Hanoi(n - 1, From, other, to)
        print(str(From) + " " + str(to))
        Hanoi(n - 1, other, to, From)


while(True):
    N = int(input())

    if(1 <= N <= 20):
        break

print(2**N - 1)
Hanoi(N, 1, 3, 2)

