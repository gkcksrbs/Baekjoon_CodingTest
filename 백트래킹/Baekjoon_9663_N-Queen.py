# 다시 풀어보기
import sys

N, Ans = int(sys.stdin.readline()), 0
H, LD, RD = [False]*N, [False]*(2*N-1), [False]*(2*N-1)

def n_queen(i):
    global Ans
    if i == N:
        Ans += 1
        return

    for j in range(N):
        if not (H[j] or LD[i+j] or RD [i-j+N-1]):
            H[j] = LD[i+j] = RD[i-j+N-1] = True
            n_queen(i+1)
            H[j] = LD[i + j] = RD[i - j + N - 1] = False

n_queen(0)
print(Ans)