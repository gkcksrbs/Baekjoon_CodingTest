from _collections import deque
import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 테스트 케이스 수 입력
t = int(input())
# 테스트 케이스 실행
for _ in range(t):
    # 팀의 수 입력
    n = int(input())
    # 작년 순위 리스트 입력
    last_rank = list(map(int, input().split()))
    # 상대적인 등수가 바뀐 쌍의 수 입력
    m = int(input())
    # 상대적인 등수가 바뀐 쌍이 없는 경우 작년 등수 그대로 출력
    if m == 0:
        for i in last_rank:
            print(i, end=' ')
        print()
    # 상대적인 등수가 바뀐 쌍이 있을 경우
    else:
        # 진입차수 리스트
        in_degree = [0] * (n+1)
        # 간선 연결 정보 리스트
        graph = [[] for _ in range(n+1)]
        # 간선 연결 정보 저장 및 진입 차수 정보 저장
        for i in range(n):
            for j in range(i+1, n):
                # 간선 연결 정보
                graph[last_rank[j]].append(last_rank[i])
                # 진입 차수 데이터
                in_degree[last_rank[i]] += 1
        # 상대적인 등수 바뀐 쌍의 수 입력 및 정보 수정
        for _ in range(m):
            # 상대적인 등수가 바뀐 두 팀 입력
            a, b = map(int, input().split())
            # 간선 연결 정보 및 진입 차수 정보 수정
            if b in graph[a]:
                graph[a].remove(b)
                in_degree[b] -= 1

                graph[b].append(a)
                in_degree[a] += 1

            else:
                graph[b].remove(a)
                in_degree[a] -= 1

                graph[a].append(b)
                in_degree[b] += 1

        # 위상 정렬 함수
        def topology_sort():
            # 올해 등수 리스트(결과값)
            result = []
            q = deque()
            # 진입 차수가 0인 노드 queue 에 삽입
            for k in range(1, n+1):
                if in_degree[k] == 0:
                    q.append(k)
            # queue 가 빌 때까지
            while q:
                now = q.popleft()
                result.append(now)
                for k in graph[now]:
                    in_degree[k] -= 1
                    if in_degree[k] == 0:
                        q.append(k)
            # 데이터에 일관성이 없는 경우 IMPOSSIBLE 출력
            if len(result) != n:
                print('IMPOSSIBLE')
            # 확실한 순위를 알 수 있는 경우 결과값 출력
            else:
                for k in range(n-1, -1, -1):
                    print(result[k], end=' ')
                print()
        # 위상 정렬 알고리즘 실행
        topology_sort()
