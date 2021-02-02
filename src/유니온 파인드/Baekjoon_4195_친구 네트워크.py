# from bisect import bisect_left, bisect_right
# import sys
# input = sys.stdin.readline
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# def count_by_range(lst, value):
#     right_index = bisect_right(lst, value)
#     left_index = bisect_left(lst, value)
#     return right_index - left_index
# t = int(input())
# for _ in range(t):
#     f = int(input())
#     name_lst = ['']
#     root = [0]
#     for _ in range(f):
#         n1, n2 = map(str, input().split())
#         if n1 not in name_lst:
#             name_lst.append(n1)
#             root.append(len(root))
#         if n2 not in name_lst:
#             name_lst.append(n2)
#             root.append(len(root))
#         union_parent(root, name_lst.index(n1), name_lst.index(n2))
#         # print(result)
import sys
# 입력 빠르게 하기 위한 변수
input = sys.stdin.readline


# 특정 원소가 속하는 집합을 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소의 집합을 합치는 함수
def union_parent(parent, number, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        parent[b] = a
        number[a] += number[b]
    # 결과값 출력
    print(number[a])


# 테스트 케이스 수 입력
t = int(input())
# 테스트 케이스 실행
for _ in range(t):
    # 친구 관계의 수 입력
    f = int(input())
    # 친구 루트 노드, 친구 관계 수 리스트
    name, num = {}, {}
    # 친구 관계 정보 입력
    for _ in range(f):
        # 두 이름 입력
        n1, n2 = map(str, input().split())
        # 입력된 이름이 없을 경우
        if n1 not in name:
            name[n1] = n1
            num[n1] = 1
        # 입력된 이름이 딕셔너리에 없을 경우
        if n2 not in name:
            name[n2] = n2
            num[n2] = 1
        # 두 집합 합치기 실행
        union_parent(name, num, n1, n2)
