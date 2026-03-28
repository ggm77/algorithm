import sys
import heapq
input = sys.stdin.readline

"""


"""

n = int(input().rstrip())

if (n == 1):
    print("0")
else:
    arr = []
    for _ in range(n):
        heapq.heappush(arr, int(input().rstrip()))

    result = 0

    while (len(arr) > 2):
        temp = heapq.heappop(arr) + heapq.heappop(arr)
        heapq.heappush(arr, temp)
        result += temp

    print(sum(arr)+result)

