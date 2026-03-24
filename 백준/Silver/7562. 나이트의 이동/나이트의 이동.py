import sys
from collections import deque
input = sys.stdin.readline

"""


"""

t = int(input().rstrip())

for _ in range(t):
    i = int(input().rstrip())

    curX, curY = map(int, input().split())

    targetX, targetY = map(int, input().split())

    que = deque([])
    visited = [([0]*(i+1)) for _ in range(i+1)]

    que.append([curX, curY, 0])
    visited[curX][curY] = 1

    while True:
        if (len(que) == 0):
            break

        temp = que.popleft()
        tempX = temp[0]
        tempY = temp[1]
        tempCnt = temp[2]

        if (tempX == targetX and tempY == targetY):
            print(tempCnt)
            break

        if (tempX+1 < i and tempY+2 < i and visited[tempX+1][tempY+2] == 0):
            visited[tempX+1][tempY+2] = 1
            que.append([tempX+1, tempY+2, tempCnt+1])
        if (tempX+2 < i and tempY+1 < i and visited[tempX+2][tempY+1] == 0):
            visited[tempX+2][tempY+1] = 1
            que.append([tempX+2, tempY+1, tempCnt+1])
        if (tempX+1 < i and tempY-2 >= 0 and visited[tempX+1][tempY-2] == 0):
            visited[tempX+1][tempY-2] = 1
            que.append([tempX+1, tempY-2, tempCnt+1])
        if (tempX+2 < i and tempY-1 >= 0 and visited[tempX+2][tempY-1] == 0):
            visited[tempX+2][tempY-1] = 1
            que.append([tempX+2, tempY-1, tempCnt+1])
        if (tempX-1 >= 0 and tempY+2 < i and visited[tempX-1][tempY+2] == 0):
            visited[tempX-1][tempY+2] = 1
            que.append([tempX-1, tempY+2, tempCnt+1])
        if (tempX-2 >= 0 and tempY+1 < i and visited[tempX-2][tempY+1] == 0):
            visited[tempX-2][tempY+1] = 1
            que.append([tempX-2, tempY+1, tempCnt+1])
        if (tempX-1 >= 0 and tempY-2 >= 0 and visited[tempX-1][tempY-2] == 0):
            visited[tempX-1][tempY-2] = 1
            que.append([tempX-1, tempY-2, tempCnt+1])
        if (tempX-2 >= 0 and tempY-1 >= 0 and visited[tempX-2][tempY-1] == 0):
            visited[tempX-2][tempY-1] = 1
            que.append([tempX-2, tempY-1, tempCnt+1])
        

