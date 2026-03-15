import sys
from collections import deque
input = sys.stdin.readline

"""


"""

def bfs(here):
    global cnt
    que = deque([here])

    cnt += 1
    visited[here] = cnt

    while (1):
        if (len(que) == 0):
            return 

        temp = que.popleft()

        for i in arr[temp]:
            if (visited[i] == 0):
                cnt += 1
                visited[i] = cnt
                que.append(i)


n, m, r = map(int, input().split())
cnt = 0

arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())

    arr[x].append(y)
    arr[y].append(x)

for i in range(n+1):
    arr[i].sort()

bfs(r)

for i in range(1, len(visited)):
    print(visited[i])
