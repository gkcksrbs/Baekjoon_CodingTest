import sys
from bisect import bisect_left, bisect_right
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 이진 탐색 함수
def binary_search(start, end, target):
    # 시작점이 끝점보다 커질 때까지
    while start <= end:
        # 중간점
        mid = (start + end) // 2
        # 리스트의 중간점 인덱스에 찾는 원소가 있으면 True 반환
        if lst[mid] == target:
            return True
        # 리스트의 중간점 인덱스의 원소가 찾는 원소보다 크다면
        elif lst[mid] > target:
            # 왼쪽 부분 탐색
            end = mid - 1
        # 리스트의 중간점 인덱스의 원소가 찾는 원소보다 작다면
        else:
            # 오른쪽 부분 탐색
            start = mid + 1
    # 리스트에 찾는 원소가 없으면 False 반환
    return False
# left_val 이상 right_val 이하인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_val, right_val):
    right_index = bisect_right(array, right_val)
    left_index = bisect_left(array, left_val)
    return right_index - left_index
# 상근이가 가지고 있는 숫자 카드 개수 입력
n = int(input())
# 상근이가 가지고 있는 숫자 카드 입력
lst = list(map(int, input().split()))
# 리스트 정렬
lst.sort()
# 찾는 숫자의 개수 입력
m = int(input())
# 찾는 숫자 리스트에 입력
search = list(map(int, input().split()))
# 결과 출력을 위한 리스트 생성
result = [0]*m
# 찾는 숫자 순차 탐색
for i in range(len(search)):
    # 찾는 숫자가 존재하는지 판별
    is_exist = binary_search(0, n-1, search[i]) # 이진 탐색 실행
    # 찾는 숫자가 존재한다면
    if is_exist:
        # 찾는 숫자의 개수 구하는 함수 실행
        result[i] = count_by_range(lst, search[i], search[i])
# 결과값 출력
for i in result:
    print(i, end=' ')
