# 집의 개수 입력
n = int(input())
# 각 집의 RGB 색깔의 비용 저장 리스트 생성
lst = []
# 각 집의 RGB 색의 비용 리스트 저장
for _ in range(n):
    lst.append(list(map(int, input().split())))
# 다이나믹 프로그래밍 실행
for i in range(1, n):
    # 이전 집의 같은 색의 비용을 제외한 다른 색의 비용을 합산한 최소값 저장
    lst[i][0] += min(lst[i-1][1], lst[i-1][2])
    lst[i][1] += min(lst[i-1][0], lst[i-1][2])
    lst[i][2] += min(lst[i-1][0], lst[i-1][1])
# 결과값 출력
print(min(lst[n-1]))
