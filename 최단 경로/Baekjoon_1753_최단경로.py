import heapq
# 무한을 의미하는 숫자로 10억으로 설정
INF = int(1e9)
# 다익스트라 알고리즘 함수
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    # 큐가 빌때까지
    while q:
        # 가장 최단의 위치 정보 꺼내기
        dis, now = heapq.heappop(q)
        # 현재 위치의 거리가 큐에서 꺼낸 거리보다 작다면 무시
        if distance[now] < dis:
            continue
        # 해당 노드 탐색
        for i in lst[now]:
            # 다음 노드로 갈때까지의 비용
            cost = distance[now] + i[1]
            # 해당 비용이 저장된 비용보다 적을 경우
            if cost < distance[i[0]]:
                # 해당 비용 저장
                distance[i[0]] = cost
                # 힙에 추가
                heapq.heappush(q, (cost, i[0]))
# 정점의 개수, 간선의 개수 입력
v, e = map(int, input().split())
# 시작점 입력
k = int(input())
# 거리 정보 리스트 무한대로 초기화
distance = [INF]*(v+1)
# 간선의 정보를 저장할 리스트 생성
lst = [[]for _ in range(v+1)]
# 간선의 정보 입력
for _ in range(e):
    # 시작점, 끝점, 비용 입력
    start, end, val = map(int, input().split())
    # 시작점 리스트에 끝점, 비용 저장
    lst[start].append((end, val))
# 다익스트라 알고리즘 실행
dijkstra(k)
# 결과값 출력
for i in range(1, v+1):
    # 해당 노드로 갈 수 업는 경우 INF 출력
    if distance[i] >= INF:
        print('INF')
    # 해당 노드로 갈 수 있는 경우 최단 경로 출력
    else:
        print(distance[i])
