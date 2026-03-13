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
        dfs(i)

n, m, r = map(int, input().split())

arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
    x, y = map(int, input().split())

    arr[x].append(y)
    arr[y].append(x)

for a in arr:
    a.sort()

dfs(r)

for i in range(1, n+1):
    print(visited[i])