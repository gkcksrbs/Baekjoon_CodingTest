import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 이진 탐색 함수(log n)
def binary_search(start, end, target):
    while start <= end:
        # 중간점
        mid = (start + end) // 2
        # 리스트의 중간점 인덱스에 찾는 원소가 있다면 True 반환
        if lst[mid] == target:
            return True
        # 리스트의 중간점 인덱스에 해당하는 숫자가 찾는 숫자보다 크다면
        elif lst[mid] > target:
            # 왼쪽 부분 탐색
            end = mid - 1
        # 리스트의 중간점 인덱스에 해당하는 숫자가 찾는 숫자보다 작다면
        else:
            # 오른쪽 부분 탐색
            start = mid + 1
    # 리스트에 찾는 숫자가 없을 경우 False 반환
    return False
# 리스트에 있는 숫자 개수 입력
n = int(input())
# 리스트 입력
lst = list(map(int, input().split()))
# 리스트 정렬(n * log n)
lst.sort()
# 찾는 숫자의 개수 입력
m = int(input())
# 찾는 숫자 입력
search = list(map(int, input().split()))

for i in search:
    # 찾는 숫자가 있는지 없는지 판별하는 변수
    result = binary_search(0, len(lst)-1, i) # 이진 탐색 실행
    # 찾는 숫자가 있으면 1 출력
    if result:
        print(1)
    # 찾는 숫자가 없으면 0 출력
    else:
        print(0)