import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""


"""

def dfs(x, y):

    if (visited[x][y] != 0):
        return
    
    visited[x][y] = 1

    if (x-1 >= 0 and arr[x-1][y] == 1):
        dfs(x-1, y)
    if (x+1 < n and arr[x+1][y] == 1):
        dfs(x+1, y)
    if (y-1 >= 0 and arr[x][y-1] == 1):
        dfs(x, y-1)
    if (y+1 < m and arr[x][y+1] == 1):
        dfs(x, y+1)

t = int(input().rstrip())

for _ in range(t):

    result = 0

    m, n, k = map(int, input().split())

    arr = [([0] * (m+1)) for _ in range(n+1)]
    visited = [([0] * (m+1)) for _ in range(n+1)]

    for _ in range(k):
        x, y = map(int, input().split())

        arr[y][x] = 1
    
    for i in range(m):
        for j in range(n):
            if (arr[j][i] == 1 and visited[j][i] == 0):
                result += 1
                dfs(j, i)

    print(result)
