# 입력 받을 숫자의 개수 N을 입력 받고 N개 만큼 좌표를 입력받는다.
# 입력 받은 수를 공백을 기준으로 숫자를 나누어 리스트에 저장하고 그 좌표들을 모아두는 리스트에 저장한다.
# lst 에 x좌표 y 좌표를 뒤집어서 저장하고 정렬한 다음에 new_lst 에 다시 뒤집어서 저장한다.
# x, y 좌표들을 문자열 형태로 출력한다.

N = int(input())

lst = []

for i in range(N):
    XY = list(map(int, input().split()))
    lst.append(XY[::-1])

lst = sorted(lst)
new_lst = []

for i in lst:
    new_lst.append(i[::-1])

for i in new_lst:
    Str = ""
    for j in i:
        Str = Str + str(j) + " "
    print(Str)
