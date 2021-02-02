import sys
# 재귀 최대 깊이 설정
sys.setrecursionlimit(50000)
# 이웃하는 배추들끼리 분류하기 위한 번호
count = 2
# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 깊이 우선 탐색
def dfs(x, y):
    graph[x][y] = count

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        # 그래프를 벗어날 경우 pass
        if nx < 0 or ny < 0 or nx >= row or ny >= col:
            continue
        # 이웃된 배추일 경우 탐색
        if graph[nx][ny] == 1:
            dfs(nx, ny)
# 테스트 케이스 개수
t = int(input())
# 테스트 케이스 실행
for i in range(t):
    # 가로, 세로, 배추의 개수
    col, row, n = map(int, input().split())
    # 그래프 생성
    graph = [[0]*col for _ in range(row)]
    for _ in range(n):
        y, x = map(int, input().split())
        graph[x][y] = 1
    # 배추 탐색
    for j in range(row):
        for k in range(col):
            if graph[j][k] == 1:
                dfs(j, k)
                count += 1
    # 필요한 배추흰지렁이의 개수 출력
    print(count-2)
    # 다음 테스트케이스를 위한 count 초기화
    count = 2