import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 도시의 수, 도시 여행 계획에 방문하는 도시 수 입력
n, m = int(input()), int(input())
# 간선 정보 저장 리스트
data = []
# 루트 노드 리스트 초기화
root = [0] * (n+1)

for i in range(n+1):
    root[i] = i
# 간선 정보 입력
for i in range(n):
    tmp = list(map(int, input().split()))

    for j in range(i+1, n):
        if tmp[j] == 1:
            data.append((i+1, j+1))


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


# 간선 정보를 탐색하여 두 노드 집합 합치기
for i, j in data:
    union_parent(root, i, j)
# 결과값 변수
result = True
# 여행 계획 리스트
schedule = list(set(map(int, input().split())))
# 여행 계획 리스트 탐색
for i in range(len(schedule)-1):
    # 현재 노드에서 다음 노드로 여행을 할 수 없을 경우
    if find_parent(root, schedule[i]) != find_parent(root, schedule[i+1]):
        # 결과값 False 저장 및 반복문 종료
        result = False
        break
# 결과값 출력
if result:
    print('YES')
else:
    print('NO')