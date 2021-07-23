# BOJ 11053 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
import sys
from bisect import bisect_left
input = sys.stdin.readline

# 수열의 길이 입력
n = int(input())
# 수열 입력
a = list(map(int, input().split()))

# DP 배열 초기화
dp = [a[0]]

# Dynamic Programming
for i in range(1, n):
    # 현재 인덱스에서의 숫자가 DP 마지막 배열보다 크다면 DP 배열 마지막에 현재 인덱스의 숫자 입력
    if dp[-1] < a[i]:
        dp.append(a[i])
    # 현재 인덱스에서의 숫자가 DP 마지막 배열보다 작거나 같다면 DP 배열에서 현재 인덱스가 들어갈 위치 찾고 삽입
    else:
        index = bisect_left(dp, a[i])
        dp[index] = a[i]

# 결과값 출력
print(len(dp))
