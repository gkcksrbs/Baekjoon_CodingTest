from _collections import deque
# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 너비 우선 탐색
def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        # 상,하,좌,우 탐색
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            # 다음 좌표가 그래프의 크기를 벗어나지 않는 경우
            if 0 <= nx < n and 0 <= ny < m:
                # 가보지 않은 미로일 경우
                if graph[nx][ny] == -1:
                    # 전 좌표 + 1
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
# 그래프의 크기 입력
n, m = map(int, input().split())
# 그래프 리스트 생성
graph = []
# 그래프 입력
for _ in range(n):
    tmp = list(map(int, input()))
    for i in range(len(tmp)):
        if tmp[i] == 1:
            # 미로의 길을 -1로 설정 후 아직 탐색하지 않은 길로 설정
            tmp[i] = -1
    graph.append(tmp)
# 시작점을 1로 설정
graph[0][0] = 1
# 너비 우선 탐색 시작
bfs(0, 0)
# n, m 좌표값 출력1
print(graph[n-1][m-1])

