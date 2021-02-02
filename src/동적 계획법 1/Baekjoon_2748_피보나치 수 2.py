import sys
# n 번째 피보나치 수를 출력받기 위한 n 입력
n = int(sys.stdin.readline())
# DP 테이블 초기화
d = [-1]*(n+1)
d[0], d[1] = 0, 1
# 다이나믹 프로그래밍 함수(피보나치 수열)
def Fibonacci(n):
    # n 번째 DP 테이블이 -1이 아니라면
    if d[n] != -1:
        # 해당 인덱스의 DP 테이블 값 반환
        return d[n]
    # n 번쨰 DP 테이블이 -1이라면
    else:
        # 피보나치 함수 재귀 실행
        d[n] = Fibonacci(n-1) + Fibonacci(n-2)
        # 해당 인덱스의 DP 테이블 값 반환
        return d[n]
# 피보나치 함수 실행 및 결과값 출력
print(Fibonacci(n))