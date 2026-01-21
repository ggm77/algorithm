import sys
input = sys.stdin.readline

# dp[i] = 마지막이 1칸인 경우 + 마지막이 2칸인 경우

n = int(input().rstrip())

if(n < 4):
    print(n%10007)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n]%10007)