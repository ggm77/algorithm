import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

heap = []

for _ in range(n):
    x = int(input().rstrip())

    if(x == 0):
        if(len(heap) == 0):
            print("0")
        else:
            print(-1*heapq.heappop(heap))
    else:
        heapq.heappush(heap, -1*x)