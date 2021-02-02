# 첫 번째로 입력 받은 숫자 N만큼 N개의 숫자를 입력 받아 리스트에 저장하고 sorted() 이용해서 정렬한다.
# 빈도수를 구하기 위해서 길이가 8001짜리인 리스트를 0으로 초기화해서 만들고 lst_2[입력된 숫자] 값에 1을 더하여 저장한다.
# lst_2에서 max() 이용하여 최대 빈도 값을 구해주고 for 루프로 최대 빈도와 같은 값인 위치들을 새로운 리스트에 저장한다.
# 그 리스트의 길이가 1일 경우 max_lst[0]을 출력해주면 되고, 아닐 경우 max_lst[1]을 출력하여 최빈값을 출력한다.


import sys

N = int(input())

lst =[]
for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst = sorted(lst)

lst_2 = [0 for i in range(8001)]

for i in lst:
    lst_2[i + 4000] += 1

max = max(lst_2)
max_lst = []
for i in range(8001):
    if max == lst_2[i]:
        max_lst.append(i-4000)


print(format(sum(lst, 0.0) / N, '.0f'))
print(lst[len(lst) // 2])
if(len(max_lst) == 1):
    print(max_lst[0])
else:
    print(max_lst[1])
print(lst[len(lst) - 1] - lst[0])
