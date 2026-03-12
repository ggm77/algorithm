import sys
import heapq
input = sys.stdin.readline

"""


"""

n = int(input().rstrip())

heap = []

for _ in range(n):
    inp = list(map(int, input().split()))

    for i in inp:
        heapq.heappush(heap, i)

        if (len(heap) >= n+1):
            heapq.heappop(heap)

print(heapq.heappop(heap))
