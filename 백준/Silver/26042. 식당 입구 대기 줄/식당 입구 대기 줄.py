import sys

n = int(sys.stdin.readline().rstrip())

queue = []
max_val = -1
num = 0

for _ in range(n):
    cmd = list(map(int, sys.stdin.readline().split()))
    if(cmd[0] == 1):
        queue.append(cmd[1])
    else:
        queue.pop(0)

    if(max_val < len(queue)):
        max_val = len(queue)
        num = queue[-1]
    elif(max_val == len(queue) and queue[-1] < num):
        num = queue[-1]

print(max_val, num)