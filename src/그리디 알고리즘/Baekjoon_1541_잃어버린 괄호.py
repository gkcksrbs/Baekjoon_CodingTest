Str = list(input().split('-'))

for i in range(len(Str)):
    Str[i] = list(map(int, Str[i].split('+')))

sum_lst = []
for i in Str:
    sum_lst.append(sum(i, 0))

if(len(sum_lst) == 1):
    print(sum_lst[0])
else:
    for i in range(1,len(sum_lst)):
        sum_lst[i] = -sum_lst[i]
    print(sum(sum_lst))
