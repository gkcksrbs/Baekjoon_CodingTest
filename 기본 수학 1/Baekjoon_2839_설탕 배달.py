# 무한대를 의미하는 값으로 10억을 설정
INF = int(1e9)
# 무게 입력
n = int(input())
# DP 테이블 초기화
dp = [INF] * 5001
dp[3] = dp[5] = 1
# 다이나믹 프로그래밍 실행
for i in range(3, n+1):
    if i+3 <= n:
        dp[i+3] = min(dp[i+3], dp[i] + 1)
    if i+5 <= n:
        dp[i+5] = min(dp[i+5], dp[i] + 1)
# 결과값 출력
if dp[n] == INF:
    print(-1)
else:
    print(dp[n])
