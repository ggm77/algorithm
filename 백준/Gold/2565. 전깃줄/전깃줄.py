import sys
input = sys.stdin.readline

"""

dp[i] = 이전 값들 중 교차하지 않는 arr[i]의 dp[i]+1의 최대값

"""

n = int(input().rstrip())

arr = [[0,0]]
for _ in range(n):
    inp1, inp2 = map(int, input().split())
    arr.append([inp1,inp2])

arr.sort(key=lambda x: x[0])

dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    max_val = 0
    for j in range(i-1, 0, -1):
        if (arr[j][1] < arr[i][1] and max_val < dp[j]):
            max_val = dp[j]
    
    dp[i] = max_val+1

print(n-max(dp))