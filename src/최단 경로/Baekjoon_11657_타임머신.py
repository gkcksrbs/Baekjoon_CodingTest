import sys
# 입력 빠르게 하기 위한 변수
input = sys.stdin.readline
# 무한대를 의미하는 값으로 10억을 지정
INF = int(1e9)
# 도시의 개수, 버스의 개수 입력
n, m = map(int, input().split())
# 최단 거리 노드 무한대로 초기화
distance = [INF] * (n+1)
# 버스 노선 리스트 초기화
lst = []
# 버스 노선 정보 입력
for _ in range(m):
    s, e, v = map(int, input().split())
    lst.append((s, e, v))


# 벨만 포드 알고리즘 함수
def bellman_ford(start):
    # 시작 노드의 최단 거리 0으로 설정
    distance[start] = 0
    # 노드의 수 만큼 탐색
    for i in range(n):
        # 버스 노선 수 만큼 탐색
        for j in range(m):
            now_node = lst[j][0]
            next_node = lst[j][1]
            cost = lst[j][2]
            # 최단 거리 리스트에 변화가 있을 경우
            if distance[now_node] != INF and distance[next_node] > distance[now_node] + cost:
                distance[next_node] = distance[now_node] + cost
                # n 번째 탐색에 변화가 있을 경우 음의 순환이 있으므로 True 반환
                if i == n-1:
                    return True
    return False


# 음의 순환 탐색을 위한 벨만 포드 알고리즘 실행
negative_cycle = bellman_ford(1)
# 음의 순환이 있을 경우 -1 출력
if negative_cycle:
    print(-1)
# 음의 순환이 없을 경우 결과값 출력
else:
    # 2번 노드부터 탐색
    for i in range(2, n+1):
        # 최단 거리가 무한대일 경우 -1 출력
        if distance[i] == INF:
            print(-1)
        # 결과값 출력
        else:
            print(distance[i])