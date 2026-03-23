import sys
from collections import deque
input = sys.stdin.readline

"""


"""

n, k = map(int, input().split())

que = deque([[n, 0]])

visited = [0] * (100001)
visited[n] = 1

while True:
    if (len(que) == 0):
        break

    val = que.popleft()
    temp = val[0]
    visited[temp] = 1

    if (temp == k):
        print(val[1])
        break

    if (temp+1 >= 0 and temp+1 < 100001 and visited[temp+1] == 0):
        que.append([temp+1, val[1]+1])
    if (temp-1 >= 0 and temp-1 < 100001 and visited[temp-1] == 0):
        que.append([temp-1, val[1]+1])
    if (temp*2 >= 0 and temp*2 < 100001 and visited[temp*2] == 0):
        que.append([temp*2, val[1]+1])

