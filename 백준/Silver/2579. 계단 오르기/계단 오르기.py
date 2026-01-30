import sys
input = sys.stdin.readline

# dp[i] = max(1칸 전 비우기, 2칸 전 비우기) -> 현재 칸은 무조건 밟기
# dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

n = int(input().rstrip())

stair = [0]
for _ in range(n):
    stair.append(int(input().rstrip()))

if(len(stair) == 2):
    print(stair[1])
elif(len(stair) == 3):
    print(stair[1]+stair[2])
else:
                
    dp = [0]*301
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

    print(dp[n])

