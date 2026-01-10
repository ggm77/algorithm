import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

# 0부터 인덱스 n-1까지의 수열에서 가장 큰 감소 부분 수열
dp = arr.copy() # 초기값: 자기 자신

for i in range(1, n):
    for j in range(i):
        if(arr[j] > arr[i]):
            if(dp[i] < dp[j]+arr[i]):
                dp[i] = dp[j] + arr[i]

print(max(dp))

