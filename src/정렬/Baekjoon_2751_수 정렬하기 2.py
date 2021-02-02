

N = int(input())

lst = []
for i in range(N):
    lst.append(int(input()))

new_lst = sorted(lst)

for i in new_lst:
    print(i)