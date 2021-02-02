from _collections import deque
# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 너비 우선 탐색
def bfs():
    global q

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 다음 좌표가 그래프의 크기를 벗어나지 않을 경우
            if 0 <= nx < n and 0 <= ny < m:
                # 다음 좌표의 토마토가 익지 않은 토마토일 경우
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
# 그래프의 크기 입력
m, n = map(int, input().split())
# 그래프 리스트 생성
graph = []
# 토마토 위치 리스트 생성
tomato = []
# 너비우선탐색을 위한 queue 생성
q = deque()
# 모든 토마토가 다 익을 날짜 저장 변수 생성
max_day = -1e9
# 모든 토마토가 다 익었는지 아닌지에 대한 변수
result = True
# 그래프 입력
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        # 익은 토마토의 좌표 리스트에 저장
        if tmp[j] == 1:
           tomato.append((i, j))
    graph.append(tmp)
# 익은 토마토의 좌표 queue 에 저장
for i in range(len(tomato)):
    x, y = tomato[i]
    q.append((x, y))
# 너비 우선 탐색 실행
bfs()

for i in range(n):
    # 상자에 익지 않은 토마토가 있을 경우
    if 0 in graph[i]:
        result = False

    max_day = max(max_day, max(graph[i]))

if result:
    print(max_day - 1)
else:
    print(-1)
