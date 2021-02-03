def check(num):
    data = str(num)
    d = 0
    for j in range(len(data)-1):
        if j == 0:
            d = int(data[j+1]) - int(data[j])
        else:
            if d != int(data[j+1]) - int(data[j]):
                return False
    return True


n = int(input())
if n < 100:
    print(n)
else:
    count = 99
    for i in range(100, n+1):
        if check(i):
            count += 1
    print(count)