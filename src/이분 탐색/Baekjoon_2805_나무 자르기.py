import sys
# 데이터와 데이터의 개수를 딕셔너리 형태로 저장해주는 Counter 클래스
from collections import Counter
# 입력 시간 빠르게 하기 위한 변수
input = sys.stdin.readline
# 나무의 수, 필요한 나무의 길이 입력
n, m = map(int, input().split())
# 나무들의 높이들을 Counter 에 입력
lst = Counter(map(int, input().split()))
# 시작점, 끝점
start, end = 0, max(lst)
# 결과값
result = 0
# 이진 탐색
while start <= end:
    # 중간점
    mid = (start + end) // 2
    # 중간점에서 자르고 남은 나무의 길이 총합 변수
    total = 0
    # i = 나무의 길이, j = 길이에 해당하는 나무의 개수
    for i, j in lst.items():
        # 자르고 남은 나무의 길이가 양수일 때
        if i - mid > 0:
            # 남은 나무의 길이 총합에 합산
            total += (i - mid) * j
    # 총 길이가 필요한 나무의 길이보다 작을 경우
    if total < m:
        # 왼쪽 부분 탐색
        end = mid - 1
    # 총 길이가 필요한 나무의 길이보다 크거나 같을 경우
    else:
        # 결과값 저장
        result = mid
        # 오른쪽 부분 탐색
        start = mid + 1
# 결과값 출력
print(result)