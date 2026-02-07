import sys
input = sys.stdin.readline

"""

dp[i] = max(
    dp[i-3] + arr[i-1]+arr[i] 마지막 2잔 마신 경우
    dp[i-2] + arr[i] 마지막 1잔 마신 경우
    dp[i-1] 안마신경우
)

"""

n = int(input().rstrip())

arr = []
for _ in range(n):
    arr.append(int(input().rstrip()))

if(n < 3):
    print(sum(arr))
else:
    dp = [0]  * (n+1)
    dp[1] = arr[0]
    dp[2] = arr[0]+arr[1]

    for i in range(3, n+1):
        dp[i] = max(
                    dp[i-3] + arr[i-2]+arr[i-1],
                    max(
                        dp[i-2] + arr[i-1],
                        dp[i-1]
                    )
                )
    
    print(dp[n])

