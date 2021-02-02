import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline


# 특정 원소가 속한 집합을 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 각 원소가 속한 집합을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수, 간선의 개수 입력
v, e = map(int, input().split())
# 루트 노드 초기화
root = [0] * (v+1)

for i in range(v+1):
    root[i] = i
# 간선의 정보 입력 리스트 초기화
data = []
# 간선의 정보 입력
for _ in range(e):
    n1, n2, c = map(int, input().split())
    data.append((c, n1, n2))
# 간선의 정보 가중치를 기준으로 정렬
data.sort()
# 결과값
result = 0
# 간선의 정보 리스트 탐색
for cost, n1, n2 in data:
    # 두 노드가 같은 집합일 경우 pass
    if find_parent(root, n1) == find_parent(root, n2):
        continue

    union_parent(root, n1, n2)
    result += cost
# 결과값 출력
print(result)
