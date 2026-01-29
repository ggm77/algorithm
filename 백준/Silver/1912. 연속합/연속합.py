import sys
input = sys.stdin.readline

# s[i] = min(s[i-1], 인덱스 0부터 i-1까지의 합)
# dp[i] = max(dp[i-1], 인덱스 0부터 i-1까지의 합-s[i])   

n = int(input().rstrip())

arr = list(map(int, input().split()))
dp = [0] * (n+1)
s = [0] * (n+1)

max_negative_val = -20000
total = 0
for i in range(len(arr)):
    if(arr[i] <= 0 and max_negative_val < arr[i]):
        max_negative_val = arr[i]
    
    total += arr[i]

    s[i+1] = min(s[i], total)
    dp[i+1] = max(dp[i], total-s[i+1])

if(dp[n] == 0):
    print(max_negative_val)
else:
    print(dp[n])

