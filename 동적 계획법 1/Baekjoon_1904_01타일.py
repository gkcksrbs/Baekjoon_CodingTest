import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# DP 테이블 초기화
d = [0]*1000001
d[1], d[2] = 1, 2
# 길이 수 입력
n = int(input())
# 01타일을 만들 수 있는 길이의 입력이 1 또는 2일 경우
if n == 1 or n == 2:
    # 결과값 출력
    print(d[n])
# 01타일을 만들 수 있는 길이의 입력이 1과 2가 아닐 경우
else:
    # 다이나믹 프로그래밍 실행
    for i in range(3, n+1):
        # 피보나치 수열 실행 후 15746으로 나눈 나머지 입력
        d[i] = (d[i-1] + d[i-2]) % 15746
    # 결과값 출력
    print(d[n])