from _collections import deque
import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 학생 수, 키를 비교한 횟수 입력
n, m = map(int, input().split())
# 진입 차수 리스트 초기화
in_degree = [0] * (n+1)
# 두 노드의 간선 정보 저장 리스트
graph = [[] for _ in range(n+1)]

q = deque()
# 결과값 리스트
result = []
# 간선 정보 입력 및 진입 차수 정보 입력
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    in_degree[n2] += 1
# 진입 차수가 0인 경우 queue 에 삽입
for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)


# 위상 정렬 알고리즘 함수
def topology_sort():
    while q:
        now = q.popleft()
        result.append(now)

        for j in graph[now]:
            in_degree[j] -= 1

            if in_degree[j] == 0:
                q.append(j)
    # 결과값 출력
    for j in result:
        print(j, end=' ')


# 위상 정렬 알고리즘 실행
topology_sort()
