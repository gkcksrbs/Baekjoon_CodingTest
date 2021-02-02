from _collections import deque
import sys
input = sys.stdin.readline
# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 너비 우선 탐색 함수
def bfs():
    q = deque()
    q.append((0, 0, 0))
    # 벽을 뚫지 않았을 때 (0, 0) 방문 완료
    visited[0][0][0] = 1
    # queue 가 빌 때까지
    while q:

        x, y, w = q.popleft()
        # 현재 좌표가 (n, m)일 경우 최단 경로 반환
        if x == n-1 and y == m-1:
            return visited[x][y][w]
        # 상,하,좌,우 탐색
        for i in range(4):
            # 다음 좌표
            nx, ny = x + dx[i], y + dy[i]
            # 다음 좌표가 그래프의 범위를 벗어나지 않을 때
            if 0 <= nx < n and 0 <= ny < m:
                # 다음 좌표에 방문하지 않았을 경우
                if not visited[nx][ny][w]:
                    # 다음 좌표가 벽일때
                    if not graph[nx][ny]:
                        # 다음 좌표 = 현재 좌표 최단 경로 + 1
                        visited[nx][ny][w] = visited[x][y][w] + 1
                        # 벽을 뚫지 않은 상태의 다음 좌표 queue 에 삽입
                        q.append((nx, ny, w))
                    # 다음 좌표가 벽이고 벽을 뚫지 않았을 때
                    elif graph[nx][ny] and not w:
                        # 다음 좌표 = 현재 좌표 최단 경로 + 1
                        visited[nx][ny][1] = visited[x][y][w] + 1
                        # 벽을 뚫은 상태의 다음 좌표 queue 에 삽입
                        q.append((nx, ny, 1))
    # 모든 경로를 탐색해도 (n, m)에 도달하지 못한 경우 -1 반환
    return -1
# 그래프의 가로, 세로 입력
n, m = map(int, input().split())
# 그래프 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))
# 벽을 뚫었을 때와 뚫지 않았을 때 2가지 경우로 나누어 3차원 방문 리스트 생성
visited = [[[0]*2for _ in range(m)]for _ in range(n)]
# 너비 우선 탐색 실행
print(bfs())