import sys
input = sys.stdin.readline
# 랜선의 개수, 필요한 랜선의 개수 입력
k, n = map(int, input().split())
# 랜선 길이 리스트 생성
wire_lst = []
# 랜선 길이 입력
for _ in range(k):
    wire_lst.append(int(input()))
# 시작점, 끝점
start, end = 1, max(wire_lst)
# 결과값
result = 0
# 이진 탐색
while start <= end:
    # 중간점
    mid = (start + end) // 2
    # 랜선을 자른 개수 변수
    total = 0
    # 자른 랜선의 개수 총합
    for i in wire_lst:
        total += i // mid
    # 총 자른 랜선의 개수가 필요한 수보다 작을 경우
    if total < n:
        # 왼쪽 부분 탐색
        end = mid - 1
    # 총 자른 랜선의 개수가 필요한 수보다 크거나 같을 경우
    else:
        # 결과값 저장
        result = mid
        # 오른쪽 부분 탐색
        start = mid + 1
# 결과값 출력
print(result)