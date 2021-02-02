import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 무한대를 의미하는 값으로 10억을 설정
INF = int(1e9)
# 마을의 수, 도로의 수 입력
v, e = map(int, input().split())
# 플로이드 와샬 알고리즘 리스트 무한대로 초기화
lst = [[INF]*(v+1) for _ in range(v+1)]
# 도로의 정보 입력
for _ in range(e):
    start, end, val = map(int, input().split())
    lst[start][end] = val
# 플로이드 와샬 알고리즘 실행
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])
# 결과값 초기화
result = INF
# 왕복 사이클 최소값 탐색
for i in range(1, v+1):
    if lst[i][i] < result:
        result = lst[i][i]
# 결과값 출력
if result == INF:
    print(-1)
else:
    print(result)
