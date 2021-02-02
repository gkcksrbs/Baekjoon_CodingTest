# import sys
# import heapq
# import copy
# INF = int(1e9)
#
#
# def dijkstra(start):
#     distance[start][0] = 0
#     q = [(0, start, distance[start][1])]
#     while q:
#         dist, now, pass_city = heapq.heappop(q)
#
#         # new_pass_city.append(now)
#         if distance[now][0] < dist:
#             continue
#         for i in lst[now]:
#             cost = i[1] + dist
#             if cost < distance[i[0]][0]:
#                 new_pass_city = []
#                 if pass_city is not None:
#                     for j in pass_city:
#                         new_pass_city.append(j)
#                 new_pass_city.append((now, i[0]))
#                 distance[i[0]][0] = cost
#                 distance[i[0]][1] = new_pass_city
#                 heapq.heappush(q, (cost, i[0], new_pass_city))
#
#
# test_num = int(input())
# for _ in range(test_num):
#     n, m, t = map(int, input().split())
#     s, g, h = map(int, input().split())
#     lst = [[] for _ in range(n+1)]
#     for _ in range(m):
#         c1, c2, val = map(int, input().split())
#         lst[c1].append([c2, val])
#         lst[c2].append([c1, val])
#     end = []
#     for _ in range(t):
#         end.append(int(input()))
#     end.sort()
#     distance = [[INF, []] for _ in range(n+1)]
#     dijkstra(s)
#     # print(distance)
#     for i in end:
#         if (g, h) in distance[i][1] or (h, g) in distance[i][1]:
#             continue
#         end.remove(i)
#     # print(distance)
#     for i in end:
#         print(i, end=' ')
#     # print()
import sys
import heapq
# 무한대를 의미하는 값으로 10억을 지정
INF = int(1e9)
# 입력을 빠르게 하기위한 변수
input = sys.stdin.readline


# 다익스트라 알고리즘 함수
def dijkstra(start):
    # 최단거리 리스트 무한대로 초기화
    distance = [INF] * (n+1)
    # 최단거리 시작지점 0으로 초기화
    distance[start] = 0
    # 다익스트라 알고리즘 실행
    q = [(0, start)]
    # 큐가 빌때까지
    while q:
        dist, now = heapq.heappop(q)
        # 해당 노드가 최단거리로 방문처리 되었을 경우 무시
        if distance[now] < dist:
            continue
        # 현재 노드의 다음 노드로 향하는 간선 탐색
        for i in lst[now]:
            cost = dist + i[1]
            # 다음 노드의 최단 거리가 현재 노드를 거쳐간 거리보다 클 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    # 최단거리 리스트 반환
    return distance


# 테스트 케이스 수 입력
test_case = int(input())
# 테스트 케이스 실행
for _ in range(test_case):
    # 교차로, 도로, 목적지 후보 수 입력
    n, m, t = map(int, input().split())
    # 출발 번호, 무조건 지나가는 도로에 이어진 교차로 입력
    s, g, h = map(int, input().split())
    # 간선의 정보 리스트 초기화
    lst = [[] for _ in range(n+1)]
    # 간선의 정보 입력
    for _ in range(m):
        c1, c2, val = map(int, input().split())
        lst[c1].append([c2, val])
        lst[c2].append([c1, val])
    # 결과 리스트
    result = []
    # 시작점, g, h 의 다익스트라 최단 거리 리스트
    start_dist = dijkstra(s)
    g_dist = dijkstra(g)
    h_dist = dijkstra(h)
    # 목적지 후보 탐색
    for _ in range(t):
        x = int(input())
        # 목적지 후보까지의 최단거리가 g, h 노드를 지날 경우
        if start_dist[g] + g_dist[h] + h_dist[x] == start_dist[x] or start_dist[h] + h_dist[g] + g_dist[x] == start_dist[x]:
            result.append(x)
    # 결과 리스트 정렬
    result.sort()
    # 결과값 출력
    for i in result:
        print(i, end=' ')



