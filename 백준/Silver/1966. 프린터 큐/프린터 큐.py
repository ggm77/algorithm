import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n, m = map(int, input().split())

    queue = deque(list(map(int, input().split())))

    cnt = 1
    while True:
        
        if(queue[0] == max(queue)):
            if(m == 0):
                print(cnt)
                break
            else:
                queue.popleft()
                m -= 1
                cnt += 1
        else:
            if(m == 0):
                m = len(queue)-1
            else:
                m -= 1
            queue.append(queue.popleft())
