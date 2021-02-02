# 테스트 케이스 수 입력
t = int(input())
# DP 테이블 초기화
d = [0]*101
d[1] = d[2] = d[3] = 1
# 다이나믹 프로그래밍 실행(피보나치 수열과 동일)
for i in range(4, 101):
    d[i] = d[i-3] + d[i-2]
# 결과값 출력
for _ in range(t):
    n = int(input())
    print(d[n])