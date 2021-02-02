# 길이 입력
n = int(input())
# DP 테이블 초기화
dp = [[0]*10 for _ in range(100)]

for i in range(10):
    dp[0][i] = 1
# 다이나믹 프로그래밍 실행
for i in range(1, 100):
    for j in range(10):
        tmp = 0
        # 리스트의 범위를 벗어나지 않도록
        if 0 <= j-1 < 10:
            tmp += dp[i-1][j-1]
        # 리스트의 범위를 벗어나지 않도록
        if 0 <= j+1 < 10:
            tmp += dp[i-1][j+1]
        dp[i][j] = tmp
# 결과값 출력
print((sum(dp[n-1]) - dp[n-1][0]) % 1000000000)
