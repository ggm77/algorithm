import sys

# 100만으로 재귀함수 확장
sys.setrecursionlimit(10**6)

def dfs(here):

    # 방문 한적 있으면 종료
    if visited[here] == 1:
        return
    
    # 방문 저장
    visited[here] = 1

    # 이어진 노드들에 대해서 dfs
    for next in tree[here]:
        if visited[next] == 0:
            result[next] = here
            dfs(next)

# 노드 개수
n = int(sys.stdin.readline().rstrip())
# 트리
tree = [[] for i in range(n+1)]

# 방문 기록
visited = [0] * (n+1)
# 결과
result = {}

# 트리 입력
for i in range(n-1):
    inp1, inp2 = map(int, sys.stdin.readline().split())

    tree[inp1].append(inp2)
    tree[inp2].append(inp1)

#dfs
dfs(1)

# 2번 노드부터 부모 노드의 번호 출력
for i in range(2, n+1):
    print(result[i])