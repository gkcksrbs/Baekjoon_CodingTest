from _collections import deque
# 컴퓨터 개수
computer = int(input())
# 컴퓨터 간 연결 개수
connect_num = int(input())
# 그래프 생성
graph = []
for i in range(computer+1):
    graph.append([])

for i in range(connect_num):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
# 그래프 정렬
for i in range(len(graph)):
    graph[i].sort()
# 컴퓨터 바이러스 방문
visited = [False] * (computer+1)
# 너비 우선 탐색
def bfs(vertex):
    q = deque()
    q.append(vertex)

    while q:
        vertex = q.popleft()
        visited[vertex] = True # 바이러스 방문 완료

        for j in range(len(graph[vertex])):
            if visited[graph[vertex][j]]: # 바이러스가 침투된 컴퓨터일 경우 pass
                continue
            if graph[vertex][j] in q: # queue 스택에 존재할 경우 pass
                continue
            q.append(graph[vertex][j]) # 인접 컴퓨터 queue 스택에 추가
    # 바이러스가 침투되지 않은 컴퓨터를 리스트에서 제거
    while False in visited:
        visited.remove(False)
    # 1번 컴퓨터를 제외한 감염된 컴퓨터 갯수 반환
    return len(visited) - 1

print(bfs(1))