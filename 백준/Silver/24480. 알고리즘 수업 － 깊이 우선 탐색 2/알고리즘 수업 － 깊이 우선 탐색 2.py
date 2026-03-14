import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""


"""

def dfs(here):
    global cnt
    if (visited[here] != 0):
        return
    
    cnt += 1
    visited[here] = cnt

    for i in arr[here]:
        if (visited[i] == 0):
            dfs(i)

n, m, r = map(int, input().split())
cnt = 0

arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())

    arr[x].append(y)
    arr[y].append(x)

for i in range(n+1):
    arr[i].sort(reverse=True)

dfs(r)

for i in range(1, len(visited)):
    print(visited[i])