import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# DP 테이블 초기화
f0 = [1, 0]
f1 = [0, 1]
# 최대 40까지 이므로 40까지 실행
for i in range(2, 41):
    f0.append(f0[i-1] + f0[i-2])
    f1.append(f1[i-1] + f1[i-2])
# 테스트 케이스 수 입력
t = int(input())
# 테스트 케이스 실행
for _ in range(t):
    # n 입력
    n = int(input())
    # 결과값 출력
    print(f0[n], f1[n])
