import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

low = 0
high = max(arr)
result = 0

while low <= high:
    mid = (low+high)//2

    cnt = 0
    for a in arr:
        temp = a-mid
        if(temp > 0):
            cnt += temp
    
    if(cnt >= m):
        result = mid
        low = mid+1
    else:
        high = mid-1

print(result)