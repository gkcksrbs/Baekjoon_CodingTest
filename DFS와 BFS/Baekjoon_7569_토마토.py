from _collections import deque
# 위,아래,앞,뒤,좌,우
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [1, -1, 0, 0, 0, 0]
# 너비 우선 탐색
def bfs():
    global q
    # queue 스택이 빌 때까지
    while q:
        x, y, z = q.popleft()

        for o in range(6):
            # 위,아래,앞,뒤,좌,우 좌표
            nx = x + dx[o]
            ny = y + dy[o]
            nz = z + dz[o]
            # 다음 좌표가 그래프의 크기를 벗어나지 않을 경우
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                # 다음 좌표의 토마토가 아직 익지 않은 토마토일 경우
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1 # 다음 날 토마토가 익음
                    q.append((nx, ny, nz)) # queue 에 추가
# 그래프의 크기 입력
m, n, h = map(int, input().split())
# 그래프 리스트 생성
graph = []
# 익은 토마토의 좌표 저장 리스트 생성
tomato = []
# 모든 토마토가 익었을 때의 날짜 저장 변수 생성
max_day = -1e9
# 상자 안의 토마토가 다 익었는지 아닌지 판별 변수
result = True
# 상자의 개수만큼 리스트 생성
for _ in range(h):
    graph.append([])
# 상자의 상태 입력
for i in range(h):
    for j in range(n):
        tmp = list(map(int, input().split()))
        for k in range(len(tmp)):
            # 익은 토마토의 좌표 저장
            if tmp[k] == 1:
                tomato.append((j, k, i))
        graph[i].append(tmp)
# 너비 우선 탐색을 위한 queue 스택 생성
q = deque(tomato)
# 너비 우선 탐색 시작
bfs()

for i in range(h):
    for j in range(n):
        # 상자 안에 익지 않은 토마토가 있을 경우
        if 0 in graph[i][j]:
            result = False
        # 모든 토마토가 다 익을때의 날짜 저장
        max_day = max(max_day, max(graph[i][j]))

if result:
    print(max_day-1)
else:
    print(-1)

