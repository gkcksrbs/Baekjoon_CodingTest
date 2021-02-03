# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)
# 도시의 개수 입력
n = int(input())
# 버스의 개수 입력
m = int(input())
# 플로이드 워셜 알고리즘 사용을 위한 그래프 리스트 무한의 값으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
# 현재 노드에서 현재 노드로 이동하는 거리는 0으로 설정
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    # 시작점, 끝점, 거리 입력
    start, end, cost = map(int, input().split())
    # 해당 그래프의 비용이 입력된 비용보다 더 크다면 해당 노드에 입력된 비용 저장
    if graph[start][end] > cost:
        graph[start][end] = cost
# 플로이드 워셜 알고리즘 실행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# 결과값 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] >= INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()