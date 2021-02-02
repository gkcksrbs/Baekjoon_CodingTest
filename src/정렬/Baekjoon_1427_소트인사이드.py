# 숫자를 문자열 형태로 입력 받고 sorted() 이용하여 리스트 lst 에 저장한다.
# 새로운 문자열 Str 초기화 해주고 for 루프로 lst 에 있는 정렬된 값들을 Str 에 더해준다.
# 역순으로 출력해준다.

N = str(input())

lst = sorted(N)

Str = ""
for i in lst:
    Str += i

print(Str[::-1])