import sys


dp = [0] * 500
dp[1] = 1
dp[2] = 2

for i in range(3, 500):
    dp[i] = dp[i-1] + dp[i-2]

while(True):
    a, b = map(int, sys.stdin.readline().split())

    if(a == 0 and b == 0):
        break

    a_index = -1
    b_index = -1

    for i in range(1, 500):
        if(a_index == -1 and a <= dp[i]):
            a_index = i
        if(b_index == -1 and b < dp[i]):
            b_index = i - 1
        if(b_index == -1 and b == dp[i]):
            b_index = i

    print(b_index - a_index + 1)
