import sys
from _collections import deque
input = sys.stdin.readline
# 나이트가 이동할 수 있는 다음 좌표
delta = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2)]
# 테스트케이스 수 입력
t = int(input())
# 테스트케이스 실행
for _ in range(t):
    # 체스판의 크기 입력
    mapSize = int(input())
    # 체스판 그래프 생성
    graph = [[-1]*mapSize for _ in range(mapSize)]
    # 해당 좌표에 나이트가 방문 했는지 체크를 위한 그래프 생성
    visited = [[False]*mapSize for _ in range(mapSize)]
    # 시작 좌표, 끝 좌표 입력
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    # 시작점과 끝점이 같을 경우 0 출력
    if sx == ex and sy == ey:
        print(0)
    else:
        # 체스판 시작점 0으로 초기화 및 방문 처리
        graph[sx][sy] = 0
        visited[sx][sy] = True
        # BFS 알고리즘 사용을 위한 Queue 생성
        q = deque()
        q.append((sx, sy))
        # BFS
        while q:
            # 현재 나이트가 있는 좌표
            px, py = q.popleft()
            # 현재 나이트가 있는 점이 끝점이랑 같을 경우 while 문 종료
            if px == ex and ey == py:
                break

            for dx, dy in delta:
                # 나이트가 이동할 수 있는 다음 좌표
                nx, ny = px + dx, py + dy
                # 다음 좌표가 그래프의 크기를 벗어나지 않을 경우
                if 0 <= nx < mapSize and 0 <= ny < mapSize:
                    # 나이트가 다음 좌표를 방문하지 않았을 때
                    if not visited[nx][ny]:
                        # 방문 처리
                        visited[nx][ny] = True
                        # 움직인 횟수 저장
                        graph[nx][ny] = graph[px][py] + 1
                        # Queue 에 삽입
                        q.append((nx, ny))
        # 결과값 출력
        print(graph[ex][ey])
