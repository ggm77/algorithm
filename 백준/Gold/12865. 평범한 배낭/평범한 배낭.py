# dp[사용가능 물건 번호][무게 허용 한도] = max(dp[사용가능 물건 개수-1][무게], dp[사용가능 물건 개수-1][무게 - 현재 무게]+현재 가치)
import sys

n, k = map(int, sys.stdin.readline().split())

items = [{"w":0,"v":0}]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    items.append({
        "w":w,
        "v":v
    })

dp = [[0]*100001 for _ in range(101)]


for i in range(1, n+1):
    item = items[i]
    for j in range(1, k+1):
        if(item.get("w") <= j):
            temp = max(dp[i-1][j], dp[i-1][j-item.get("w")]+item.get("v"))
            if(dp[i][j] < temp):
                dp[i][j] = temp
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])