import sys
# 입력 빠르게 하기 위한 변수
input = sys.stdin.readline
# 노드의 개수, 연산 개수 입력
n, m = map(int, input().split())
# 루트 노드 초기화
root = [0] * (n+1)

for i in range(1, n+1):
    root[i] = i


# 특정 원소가 속한 집합을 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소의 집합을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 연산 수행
for _ in range(m):
    # 연산의 종류, 두 노드 입력
    op, n1, n2 = map(int, input().split())
    # 합치는 연산일 경우
    if op == 0:
        union_parent(root, n1, n2)
    # 두 원소가 같은 집합에 속하는지 확인하는 연산일 경우
    else:
        # 같은 집합인 경우 YES, 다른 집합인 경우 NO 출력
        if find_parent(root, n1) == find_parent(root, n2):
            print('YES')
        else:
            print('NO')
