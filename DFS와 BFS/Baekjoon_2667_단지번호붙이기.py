# 지도의 크기
n = int(input())
# 지도 생성
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 단지 번호
num = 2
# 깊이 우선 탐색
def dfs(x, y):
    # 단지 설정
    graph[x][y] = num
    # 상하좌우 탐색
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 지도의 크기를 벗어나면 pass
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        # 현재 위치의 집과 연결된 집일 경우
        if graph[nx][ny] == 1:
            dfs(nx, ny)
# 집 탐색
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 집일 경우
            dfs(i, j) # 이웃하는 집 탐색
            num += 1 # 다음 단지
# 출력될 결과
result = []
for i in range(n):
    for j in range(n):
        result.append(graph[i][j])

print(max(result)-1) # 총 단지 개수 출력
# 각 단지 집의 개수 저장
lst = []
for i in range(2, max(result)+1):
    lst.append(result.count(i))
# 각 단지 집의 개수 정렬
lst.sort()
# 각 단지 집의 개수 출력
for i in range(len(lst)):
    print(lst[i])