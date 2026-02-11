import sys
input = sys.stdin.readline

"""

"""

n, m = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] * (n+1)

sum_val = 0
for i in range(1,n+1):
    sum_val += arr[i-1]
    dp[i] = sum_val

for _ in range(m):
    start, end = map(int, input().split())

    print(dp[end]-dp[start]+arr[start-1])
