from _collections import deque
# 너비 우선 탐색
def bfs():
    q = deque()
    # queue 스택에 현재 위치와 이동 횟수 추가
    q.append((n, 0))

    while q:
        val, count = q.popleft()
        # 방문하지 않은 위치일 경우
        if not visited[val]:
            # 방문 완료
            visited[val] = True
            # 동생의 위치와 같을 경우 횟수 반환
            if val == k:
                return count
            # 현재 인덱스의 두배의 인덱스가 100000을 넘지 않을 경우 queue 스택에 추가
            if val*2 <= 100000:
                q.append((val*2, count+1))
            # 현재의 인덱스의 다음 인덱스가 100000을 넘지 않을 경우 queue 스택에 추가
            if val+1 <= 100000:
                q.append((val+1, count+1))
            # 현재의 인덱스의 이전 인덱스가 0을 넘을 경우 queue 스택에 추가
            if val-1 >= 0:
                q.append((val-1, count+1))
# 수빈이와 동생의 위치 인덱스 입력
n, k = map(int, input().split())
# 방문 확인 리스트
visited = [False for _ in range(100001)]
# 너비 우선 탐색 실행
print(bfs())

