import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 두 점 사이의 거리 계산 함수


def distance(loc1, loc2):
    return ((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)**0.5


# 특정 원소가 속한 집합을 찾는 함수
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


# 각 원소가 속한 집합을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 별의 개수 입력
n = int(input())
# 별의 위치 리스트
loc = []
# 두 별 간의 거리 정보 리스트
data = []
# 루트 노드 리스트 초기화
root = [0] * (n+1)

for i in range(n+1):
    root[i] = i
# 각 별의 좌표 입력
for _ in range(n):
    x, y = map(float, input().split())
    loc.append((x, y))
# 두 별 간의 거리 정보 리스트 저장
for i in range(len(loc)):
    for j in range(i+1, len(loc)):
        data.append((distance(loc[i], loc[j]), i, j))
# 거리 순으로 거리 정보 리스트 정렬
data.sort()
# 결과값
result = 0.0
# 거리 정보 리스트 탐색
for cost, n1, n2 in data:
    # 두 별이 같은 집합에 속하는 경우
    if find_parent(root, n1) == find_parent(root, n2):
        continue
    union_parent(root, n1, n2)
    result += cost
# 결과값 출력
print(round(result, 2))
