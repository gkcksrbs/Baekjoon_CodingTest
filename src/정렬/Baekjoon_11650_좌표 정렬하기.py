# 입력 받을 숫자의 개수 N을 입력 받고 N개 만큼 좌표를 입력받는다.
# 입력 받은 수를 공백을 기준으로 숫자를 나누어 리스트에 저장하고 그 좌표들을 모아두는 리스트에 저장한다.
# sorted() 이용하여 좌표들이 모인 리스트들을 정렬하고 출력할 때 문자열 형태로 출력한다.

N = int(input())

lst = []

for i in range(N):
    XY = list(map(int, input().split()))
    lst.append(XY)

lst = sorted(lst)

for i in lst:
    Str = ""
    for j in i:
        Str = Str + str(j) + " "
    print(Str)