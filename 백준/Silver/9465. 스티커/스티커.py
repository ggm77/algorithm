import sys
input = sys.stdin.readline

"""

dp[몇번째 스티커까지인지][어떤 스티커 썼는지]

안쓰는 경우
dp[n][0] = max(dp[n-1][0], dp[n-1][1], dp[n-1][2])

1번 쓰는 경우
dp[n][1] = max(dp[n-1][0] + arr[n-1][0], dp[n-1][2] + arr[n-1][0])

2번 쓰는 경우
dp[n][2] = max(dp[n-1][0] + arr[n-1][1], dp[n-1][1] + arr[n-1][1])

"""

t = int(input().rstrip())

for _ in range(t):

    n = int(input().rstrip())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))

    dp = [([0] * 3) for _ in range(n+1)]
    dp[1][0] = 0
    dp[1][1] = arr[0][0]
    dp[1][2] = arr[1][0]

    for i in range(2, n+1):
        dp[i][0] = max(dp[i-1][0], max(dp[i-1][1], dp[i-1][2]))
        dp[i][1] = max(dp[i-1][0] + arr[0][i-1], dp[i-1][2] + arr[0][i-1])
        dp[i][2] = max(dp[i-1][0] + arr[1][i-1], dp[i-1][1] + arr[1][i-1])
    
    print(max(dp[n][0], max(dp[n][1], dp[n][2])))    
