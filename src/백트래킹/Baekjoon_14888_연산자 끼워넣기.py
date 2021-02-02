#시간 초과
# import sys
# from _collections import deque
#
# def change_Op(lst):
#     Op_lst = []
#     for i in range(4):
#         for j in range(lst[i]):
#             if i == 0:
#                 Op_lst.append('+')
#             elif i == 1:
#                 Op_lst.append('-')
#             elif i == 2:
#                 Op_lst.append('*')
#             else:
#                 Op_lst.append('/')
#     return Op_lst
#
# def Op_case(lst):
#     if len(lst) == 0:
#         return [lst]
#     else:
#         case = []
#         for i in lst:
#             tmp = lst.copy()
#             tmp.remove(i)
#             tmp.sort()
#             for j in Op_case(tmp):
#                 j.insert(0, i)
#                 if j not in case:
#                     case.append(j)
#         return case
#
# N = int(sys.stdin.readline())
# A = deque(map(int, sys.stdin.readline().split()))
# Op_num = change_Op(list(map(int, sys.stdin.readline().split())))
# case_lst = Op_case(Op_num)
# temp = []
#
# for i in range(len(case_lst)):
#     B = A.copy()
#     result = B.popleft()
#     for j in range(len(case_lst[i])):
#         if case_lst[i][j] == '+':
#             result += B.popleft()
#         elif case_lst[i][j] == '*':
#             result *= B.popleft()
#         elif case_lst[i][j] == '-':
#             result -= B.popleft()
#         elif case_lst[i][j] == '/':
#             if result < 0:
#                 result = result // B.popleft() +1
#             else:
#                 result //= B.popleft()
#     temp.append(result)
#
# print(max(temp))
# print(min(temp))

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

Max = -1e9
Min = 1e9


def DFS(index, now):
    global add, sub, mul, div, Max, Min

    if (index == N):
        Max = max(Max, now)
        Min = min(Min, now)

    else:
        if add > 0:
            add -= 1
            DFS(index+1, now + A[index])
            add += 1

        if sub > 0:
            sub -= 1
            DFS(index+1, now - A[index])
            sub += 1

        if mul > 0:
            mul -= 1
            DFS(index+1, now * A[index])
            mul += 1

        if div > 0:
            div -= 1
            DFS(index+1, int(now / A[index]))
            div += 1

DFS(1, A[0])

print(Max)
print(Min)