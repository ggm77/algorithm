import sys
input = sys.stdin.readline

k, n = map(int, input().split())

arr = []
for _ in range(k):
    arr.append(int(input().rstrip()))

low = 1
high = max(arr)
result = 0

while low <= high:
    mid = (low+high)//2

    cnt = 0
    for a in arr:
        cnt += a//mid
    
    if(cnt < n):
        high = mid-1
    else:
        result = mid
        low = mid+1

print(result)