import sys
from bisect import bisect_left
# 입력 시간 빠르게 하기 위한 변수
input = sys.stdin.readline
# 수열의 크기 입력
n = int(input())
# 수열 리스트 입력
lst = list(map(int, input().split()))
lst.insert(0, 0)
# 인덱스를 수열 길이로 하고 그 위치를 저장하는 리스트
x = [0]
# 모든 수열 탐색
for i in range(1, n+1):
    # x 리스트의 마지막 값이 해당 수열 값보다 작다면
    if x[-1] < lst[i]:
        # x 리스트에 해당 수열 값 입력
        x.append(lst[i])
    # x 리스트의 마지막 값이 해당 수열 값보다 크거나 같다면
    else:
        # 해당 인덱스 이분 탐색
        index = bisect_left(x, lst[i])
        # x 에서의 인덱스에 해당 수열 값 입력
        x[index] = lst[i]
# 결과값 출력
print(len(x)-1)
