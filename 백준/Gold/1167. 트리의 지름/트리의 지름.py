import sys

# 재귀함수 100만으로 확장
sys.setrecursionlimit(10**6)

def dfs(here, distance):
    global max_distance
    global max_distance_index

    # 방문한적 있으면 종료
    if(visited[here] == 1):
        return
    
    # 방문 저장
    visited[here] = 1

    # 연결된 노드 중 방문 안한거 있으면 방문
    for next in tree[here]:
        if(visited[next[0]] == 0):
            dfs(next[0], distance+next[1])

    # 현재 노드에서 최대 거리면 저장
    if(max_distance < distance):
        max_distance = distance
        max_distance_index = here

    return

# v입력
v = int(sys.stdin.readline().rstrip())
tree = {}
visited = [0] * (v+1)

# 최대 거리 측정용 변수
max_distance = -1
max_distance_index = -1


# 트리 입력
for _ in range(v):
    temp = list(map(int, sys.stdin.readline().split()))

    tree[temp[0]] = []

    i = 1
    while(i < len(temp) and temp[i] != -1):
        tree[temp[0]].append([temp[i], temp[i+1]])
        i += 2

# 첫번째 dfs, 두 지름 정점 중 하나 찾기
dfs(1, 0)

# 방문기록 삭제
visited = [0] * (v+1)

# 최대 거리 초기화
max_distance = -1

# 두번째 dfs, 찾아낸 한쪽 정점으로 반대쪽 찾기
dfs(max_distance_index, 0)

print(max_distance)
