import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline


# 특정 원소가 속한 집합을 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 테스트 케이스 수 입력
t = int(input())
# 테스트 케이스 실행
for _ in range(t):
    # 나라의 개수, 비행기의 개수 입력
    n, m = map(int, input().split())
    # 간선 정보 저장 리스트
    data = []
    # 루트 노드 리스트 초기화
    root = [0] * (n+1)

    for i in range(n+1):
        root[i] = i
    # 간선의 정보 입력
    for _ in range(m):
        n1, n2 = map(int, input().split())
        data.append((n1, n2))
    # 결과값 초기화
    result = 0
    # 간선 정보 탐색
    for n1, n2 in data:
        if find_parent(root, n1) == find_parent(root, n2):
            continue
        union_parent(root, n1, n2)
        result += 1
    # 결과값 출력
    print(result)
