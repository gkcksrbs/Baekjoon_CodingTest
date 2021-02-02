import heapq
import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)


# 다익스트라 알고리즘 함수
def dijkstra(start):
    # 시작 지점에서부터 다른 노드까지의 최단거리 리스트 무한대로 초기화
    distance = [INF]*(n+1)
    # 시작 지점은 0으로 초기화
    distance[start] = 0
    q = [(0, start)]
    # 큐가 빌때까지
    while q:
        dist, now = heapq.heappop(q)
        # 다음 노드에 대한 최단 거리가 이미 탐색 되었을 때 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 이어진 다른 노드 탐색
        for i in lst[now]:
            cost = dist + i[1]
            # 다음 노드까지의 최단 거리보다 현재 노드를 거쳐간 거리가 더 짧을 경우
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    # 최단 거리 리스트 반환
    return distance


# 정점의 개수, 간선의 개수 입력
n, e = map(int, input().split())
# 간선의 정보 리스트 초기화
lst = [[] for _ in range(n + 1)]
# 간선의 정보 입력
for _ in range(e):
    c1, c2, val = map(int, input().split())
    lst[c1].append([c2, val])
    lst[c2].append([c1, val])
# 거쳐가야 할 두 노드 입력
v1, v2 = map(int, input().split())
# 1, v1, v2 노드의 최단 거리 리스트
one = dijkstra(1)
d1 = dijkstra(v1)
d2 = dijkstra(v2)
# 결과값 저장
result = min(one[v1] + d1[v2] + d2[n], one[v2] + d2[v1] + d1[n])
# 결과값 출력
if result >= INF:
    print(-1)
else:
    print(result)
