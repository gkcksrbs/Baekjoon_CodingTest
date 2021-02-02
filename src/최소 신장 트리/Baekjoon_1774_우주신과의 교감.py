import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline


# 두 점 사이의 거리 반환 함수
def distance(node1, node2):
    return((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2) ** 0.5


# 특정 원소가 속하는 집합을 찾는 함수
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


# 각 원소가 속한 집합들을 하나의 집합으로 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 우주신들의 개수와 이미 연결된 신들과의 통로의 개수 입력
n, m = map(int, input().split())
# 각 우주신들의 좌표 저장 리스트
loc = [()]
# 각 노드의 간선 정보 저장 리스트
data = []
# 루트 노드 최기화
root = [i for i in range(n+1)]
# 각 노드의 좌표 입력
for _ in range(n):
    x, y = map(int, input().split())
    loc.append((x, y))
# 이미 연결된 신들과의 통로에 대한 두 노드 합치기
for _ in range(m):
    n1, n2 = map(int, input().split())
    if find_parent(root, n1) != find_parent(root, n2):
        union_parent(root, n1, n2)
# 두 노드간의 간선 정보 저장
for i in range(1, n+1):
    for j in range(i+1, n+1):
        data.append((distance(loc[i], loc[j]), i, j))
# 간선 정보 저장 리스트 거리순으로 정렬
data.sort()
# 결과값
result = 0.0
# 간선 정보 탐색
for cost, n1, n2 in data:
    # 두 노드가 같은 집합에 속해 있는 경우 pass
    if find_parent(root, n1) == find_parent(root, n2):
        continue
    union_parent(root, n1, n2)
    result += cost
# 결과값 출력
print(format(result, ".2f"))
