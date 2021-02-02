# 포도주 잔의 개수 입력
n = int(input())
# 포도주 양 리스트 생성 및 입력
lst = []
for _ in range(n):
    lst.append(int(input()))
# 포도주 잔의 개수가 1일 때
if n == 1:
    print(lst[0])
# 포도주 잔의 개수가 2일 때
elif n == 2:
    print(lst[0] + lst[1])
# 포도주 잔의 개수가 1과 2가 아닐 때
else:
    # DP 테이블 초기화
    dp = [0] * (n+1)
    dp[1] = lst[0]
    dp[2] = lst[0] + lst[1]
    # 다이나믹 프로그래밍 실행
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-3]+lst[i-2]+lst[i-1], dp[i-2]+lst[i-1])
    # 결과값 출력
    print(max(dp))