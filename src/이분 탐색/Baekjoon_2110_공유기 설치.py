import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 집의 개수, 공유기의 개수 입력
n, c = map(int, input().split())
# 집 그래프 리스트 생성
lst = []
# 집 그래프 리스트 입력
for _ in range(n):
    lst.append(int(input()))
# 집 그래프 리스트 정렬
lst.sort()
# 두 공유기 사이의 거리 최대, 최소
start = lst[1] - lst[0]
end = lst[-1] - lst[0]
# 결과값
result = 0
# 이분 탐색 실행
while start <= end:
    # 두 공유기 사이의 거리 중간점
    mid = (start + end) // 2
    # 두 공유기의 거리를 재기 위한 첫 번째 공유기를 설치한 집
    tmp = lst[0]
    # 설치 가능한 공유기 개수
    count = 1
    # 모든 집 탐색
    for i in range(1, n):
        # 두 집 사이의 거리가 중간점보다 크거나 같을 경우
        if lst[i] - tmp >= mid:
            tmp = lst[i]
            # 공유기 개수 + 1
            count += 1
    # 총 설치한 공유기의 개수가 설치하려고 할 공유기의 개수보다 적을 경우
    if count < c:
        # 왼쪽 부분 탐색
        end = mid - 1
    # 총 설치한 공유기의 개수가 설치하려고 할 공유기의 개수보다 크거나 같을 경우
    else:
        # 오른쪽 부분 탐색
        start = mid + 1
        # 결과값 저장
        result = mid
# 결과값 출력
print(result)