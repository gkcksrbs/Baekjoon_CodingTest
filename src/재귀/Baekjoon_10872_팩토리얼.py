def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)

while(True):
    N = int(input())

    if(0<=N<=12):
        break
print(factorial(N))