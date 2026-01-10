money = [7, 5, 2, 1]

n = int(input())
result = 0

dp = [0] * (n+1)

for i in range(1,n+1):
    min_value = 1000000
    for m in money:
        if(i-m >= 0):
            temp = dp[i-m]+1
            if(temp < min_value):
                min_value = temp
    dp[i] = min_value

print(dp[n])