import sys
input = sys.stdin.readline

"""

dp[여기까지 사용할 수 있음][현재 값 사용 여부]

dp[n][0] = max(dp[n-1][0], dp[n-1][1])

dp[n][1] = max(dp[현재 값보다 작은 수 번호][1]) + 현재 값
-> 현재 값보다 작은거 없으면 dp[n][1] = 현재 값

"""

n = int(input().rstrip())

arr = list(map(int, input().split()))

dp = [([0] * 2) for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = arr[0]

for i in range(2, n+1):
    index = -1
    max_val = -1
    for j in range(i-2, -1, -1):
        if(arr[j] < arr[i-1] and max_val < dp[j+1][1]):
            index = j
            max_val = dp[j+1][1]
    
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])

    if(index != -1):
        dp[i][1] = dp[index+1][1] + arr[i-1]
    else:
        dp[i][1] = arr[i-1]


print(max(dp[n][0], dp[n][1]))