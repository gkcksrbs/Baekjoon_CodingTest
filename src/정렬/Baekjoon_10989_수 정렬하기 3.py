# 처음에 입력된 숫자 만큼 10000이하의 자연수를 입력 받아 수를 정렬하여 출력한다.
# 길이가 10001짜리인 리스트를 0으로 초기화 한 하나를 만들어서 숫자를 입력 받을 때마다 lst[입력 받은 숫자]에 1을 증가시켜준다.
# for 루프로 0부터 10001까지 lst[i]값이 0이 아닐 때 lst[i]에 해당하는 숫자만큼 반복출력한다.


import sys

N = int(input())

lst = [0 for i in range(10001)]

for i in range(N):
    lst[int(sys.stdin.readline())] += 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)
