import sys
import heapq
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 무한대를 의미하는 값으로 10억을 설정
INF = int(1e9)


# 다익스트라 최단거리 알고리즘 함수
def dijkstra(start):
    # q = [(0, start, 0)]
    # while q:
    #     dist, now, cost = heapq.heappop(q)
    #     if dp[now][cost] < dist:
    #         continue
    #     for j in lst[now]:
    #         new_cost = cost + j[2]
    #         time = dist + j[1]
    #         if new_cost > m:
    #             continue
    #
    #         # if 0 <= new_cost <= m:
    #         if dp[j[0]][new_cost] > time:
    #             dp[j[0]][new_cost] = time
    #             heapq.heappush(q, (time, j[0], new_cost))
    for i in range(m+1):
        for j in range(1, n+1):
            if dp[j][i] == INF:
                continue
            for o in lst[j]:
                if i + o[1] > m:
                    continue
                dp[o[0]][i+o[1]] = min(dp[o[0]][i+o[1]], dp[j][i] + o[2])


# 테스트 케이스 수 입력
t = int(input())
# 테스트 케이스 실행
for _ in range(t):
    # 공항의 수, 총 지원비용, 티켓 정보의 수 입력
    n, m, k = map(int, input().split())
    # DP 테이블 무한대로 초기화 후 1번 공항의 0번째 리스트는 0으로 초기화
    dp = [[INF]*(m+1) for _ in range(n+1)]
    dp[1][0] = 0
    # 티켓 정보 저장 리스트
    lst = [[] for _ in range(n+1)]
    # 티켓 정보 입력
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        lst[u].append([v, c, d])
    # 다익스트라 알고리즘 실행
    dijkstra(1)
    # 결과값
    result = min(dp[n])
    # 결과값 출력
    if result >= INF:
        print("Poor KCM")
    else:
        print(result)
