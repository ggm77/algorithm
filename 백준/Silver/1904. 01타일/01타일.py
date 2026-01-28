import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

prev1 = 2
prev2 = 3
curr = 4

if(n < 4):
    print(n)
else:
    # dp[i] = dp[i-1] + dp[i-2]
    for i in range(4, n+1):
        curr = (prev1 + prev2)%15746
        prev1 = prev2
        prev2 = curr

    print(curr)