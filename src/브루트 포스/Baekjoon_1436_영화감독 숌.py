# 정수 n 입력
n = int(input())

num = 666
# 결과값 리스트
result = []

while len(result) != n:
    if '666' in str(num):
        result.append(num)
    num += 1
# 결과값 출력
print(result[n-1])