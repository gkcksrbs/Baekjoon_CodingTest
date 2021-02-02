def Fibonacci(n):
    if (n == 0):
        return 0
    if(n == 1):
        return 1
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))

while(True):
    N = int(input())

    if(0 <= N <=20):
        break

print(Fibonacci(N))
