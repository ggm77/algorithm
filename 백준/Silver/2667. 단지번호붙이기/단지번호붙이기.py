import sys
input = sys.stdin.readline

"""


"""

def dfs(x, y):

    if (visited[x][y] == 1):
        return 0

    temp = 0
    visited[x][y] = 1

    if (arr[x][y] == 1):
        temp += 1

    if (x+1 < n and visited[x+1][y] == 0 and arr[x+1][y] == 1):
        temp += dfs(x+1, y)
    if (x-1 >= 0 and visited[x-1][y] == 0 and arr[x-1][y] == 1):
        temp += dfs(x-1, y)
    if (y+1 < n and visited[x][y+1] == 0 and arr[x][y+1] == 1):
        temp += dfs(x, y+1)
    if (y-1 >= 0 and visited[x][y-1] == 0 and arr[x][y-1] == 1):
        temp += dfs(x, y-1)

    return temp

n = int(input().rstrip())

visited = [([0] * (n+1)) for _ in range(n+1)]

result = []

arr = []
for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))

for i in range(n):
    for j in range(n):
        if (arr[i][j] == 1):
            r = dfs(i, j)
            if (r != 0):
                result.append(r)

result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])

