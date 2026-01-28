import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

queue = deque([[0,0,1]])
visited = [([0]*101) for _ in range(101)]

while True:

    curr = queue.popleft()
    x = curr[0]
    y = curr[1]
    step = curr[2]

    if(x == n-1 and y == m-1):
        print(step)
        break

    if(visited[x][y] == 1):
        continue

    visited[x][y] = 1

    if(x+1 < n and arr[x+1][y] != 0):
        queue.append([x+1, y, step+1])
    if(x-1 >= 0 and arr[x-1][y] != 0):
        queue.append([x-1, y, step+1])
    if(y+1 < m and arr[x][y+1] != 0):
        queue.append([x, y+1, step+1])
    if(y-1 >= 0 and arr[x][y-1] != 0):
        queue.append([x, y-1, step+1])

