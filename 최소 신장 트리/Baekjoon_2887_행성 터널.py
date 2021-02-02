import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 행성의 개수 입력
n = int(input())
# 루트 노드 초기화
root = [0] * n

for i in range(n):
    root[i] = i
# 행성의 좌표 리스트
loc = [[]for _ in range(3)]
# 행성의 좌표 입력
for i in range(n):
    x, y, z = map(int, input().split())
    loc[0].append((x, i))
    loc[1].append((y, i))
    loc[2].append((z, i))
# 행성 좌표 정렬
for i in range(3):
    loc[i].sort()
# 간선 정보 리스트
data = []
# 간선 정보 입력
for i in range(3):
    for j in range(n-1):
        data.append((abs(loc[i][j][0] - loc[i][j+1][0]), loc[i][j][1], loc[i][j+1][1]))
# 간선 정보 정렬
data.sort()


# 특정 원소가 속한 집합을 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소 집합을 합치는 함수
def union_parent(parent, n1, n2):
    n1 = find_parent(parent, n1)
    n2 = find_parent(parent, n2)
    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2


# 결과값
result = 0
# 최소 스패닝 트리 알고리즘 실행
for cost, s, e in data:
    if find_parent(root, s) == find_parent(root, e):
        continue

    union_parent(root, s, e)
    result += cost
# 결과값 출력
print(result)
