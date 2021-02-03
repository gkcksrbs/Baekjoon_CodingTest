data = [True] * 10001
for i in range(1, 10001):
    tmp = str(i)
    next_num = i
    for j in tmp:
        next_num += int(j)
    if next_num < 10001:
        data[next_num] = False
for i in range(1, 10001):
    if data[i]:
        print(i)