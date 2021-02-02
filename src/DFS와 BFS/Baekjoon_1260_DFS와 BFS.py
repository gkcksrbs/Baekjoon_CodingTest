from _collections import deque
# 점의 개수, 선의 개수, 시작점
n, m, v = map(int, input().split())
# 그래프 생성
graph = []
for i in range(n+1):
    graph.append([])
# 선의 시작점과 끝점
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
# 그래프 정렬
for i in range(len(graph)):
    graph[i].sort()
# 점의 방문
visited = [False]*(n+1)
dfs_lst = []
# 너비 우선 탐색
def bfs(vertex):
    q = deque()
    q.append(vertex)
    result = ""

    while q:
        vertex = q.popleft()
        result += str(vertex) + " "
        visited[vertex] = True # 현재 vertex 방문 완료

        for j in range(len(graph[vertex])):
            # 방문한 vertex 일 경우 pass
            if visited[graph[vertex][j]]:
                continue
            # queue 에 존재할 경우 pass
            if graph[vertex][j] in q:
                continue
            q.append(graph[vertex][j])

    return result
# 깊이 우선 탐색
def dfs(vertex):
    visited[vertex] = True # 현재 vertex 방문 완료
    dfs_lst.append(vertex)

    for j in range(len(graph[vertex])):
        if visited[graph[vertex][j]]:
            continue # 방문한 vertex 일 경우 pass
        dfs(graph[vertex][j])

dfs(v)
for i in range(len(dfs_lst)):
    print(dfs_lst[i], end=" ")
print()
for i in range(len(visited)):
    visited[i] = False
print(bfs(v))
