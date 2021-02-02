import sys
# 입력 빠르게 하기 위한 변수
input = sys.stdin.readline
# 배열의 크기 입력
n = int(input())
# 배열 B 에서의 해당 인덱스값 입력
k = int(input())
# 시작점, 끝점
start = 1
end = n*n
# 결과값
result = 0
# 이분 탐색 실행
while start <= end:
    # 중간점
    mid = (start + end) // 2
    # 중간점보다 작은 수를 세기 위한 변수
    count = 0
    # 개수 세기
    for i in range(1, n+1):
        count += min(mid // i, n)
    # 중간점보다 작은 수의 개수가 해당 인덱스의 값보다 작다면
    if count < k:
        # 오른쪽 부분 탐색
        start = mid + 1
    # 중간점보다 작은 수의 개수가 해당 인덱스의 값보다 크거나 같다면
    else:
        # 왼쪽 부분 탐색
        end = mid - 1
        # 결과값 저장
        result = mid
# 결과값 출력
print(result)
