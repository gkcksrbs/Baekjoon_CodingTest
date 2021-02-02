# 입력 개수 N을 입력하고 문자열의 길이는 50까지 이므로 50까지 리스트를 만들어주고 리스트 안에 또 리스트를 생성한다.
# 리스트에 lst[입력 받은 문자열의 길이]에 문자열을 추가하여 저장한다.
# for 루프로 각 리스트 안에 중복되는 것을 set()으로 제거하고 sorted()로 정렬한다.
# 각 문자열들을 문자열의 길이 순서대로 출력한다.

N = int(input())

lst = [[] for i in range(51)]

for i in range(N):
    Str = input()
    Len = len(Str)
    lst[Len].append(Str)

for i in range(51):
    if(lst[i] != None):
        lst[i] = list(set(lst[i]))
        lst[i] = sorted(lst[i])


for i in range(51):
    if lst[i] != None:
        for j in lst[i]:
            print(j)