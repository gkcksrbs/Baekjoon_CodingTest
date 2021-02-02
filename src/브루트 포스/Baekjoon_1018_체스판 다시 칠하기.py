from _collections import deque
import sys
# input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
board = []
result = []
for _ in range(n):
    board.append(list(str(input())))
for a in range(n - 7):
    for i in range(m - 7):
        tmp1 = 0
        tmp2 = 0
        for b in range(a, a+8):
            for j in range(i, i+8):
                if (j + b) % 2 == 0:
                    if board[b][j] != 'W':
                        tmp1 += 1
                    if board[b][j] != 'B':
                        tmp2 += 1
                else:
                    if board[b][j] != 'B':
                        tmp1 += 1
                    if board[b][j] != 'W':
                        tmp2 += 1
        result.append(tmp1)
        result.append(tmp2)
print(result)
print(min(result))

