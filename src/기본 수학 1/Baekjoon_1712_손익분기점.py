# 고정비용, 노트북 생산 비용, 판매 비용 입력
a, b, c = map(int, input().split())
# 결과값 출력
if c-b <= 0:
    print(-1)

else:
    result = a // (c-b)
    print(result + 1)
