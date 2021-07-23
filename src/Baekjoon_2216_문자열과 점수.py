# Sequence Alignment
score = list(map(int, input().split()))
str1 = input()
str2 = input()
#
dp = [[0]*(len(str1)+1) for i in range(len(str2)+1)]

# DP 초기화(공백 감점)
for i in range(1, len(str1)+1):
    dp[0][i] = dp[0][i-1] + score[1]
for i in range(1, len(str2)+1):
    dp[i][0] = dp[i-1][0] + score[1]

# 같은 문자이면 왼쪽 대각선 위 + 맞은 점수, 다른 문자면 max(아래 - 공백 점수, 왼쪽 - 공백 점수, 대각선 위- 틀린 점수)
for i in range(1, len(str2)+1):
    for j in range(1, len(str1) + 1):
        if str1[j-1] == str2[i-1]:
            dp[i][j] = dp[i-1][j-1] + score[0]
        else:
            dp[i][j] = max(dp[i-1][j-1] + score[2], dp[i-1][j] + score[1], dp[i][j-1] + score[1])
print(dp[-1][-1])

