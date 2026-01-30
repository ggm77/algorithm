import sys
input = sys.stdin.readline

# dp[위 부터 몇번째 층][몇번째 잎]
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) -> j와 j-1이 리스트 범위 내인 경우

dp = [([0]*501) for _ in range(501)]

n = int(input().rstrip())

inp = int(input().rstrip())
dp[1][1] = inp

for i in range(2, n+1):
    inp = list(map(int, input().split()))

    for j in range(1, len(inp)+1):
        dp[i][j] = max(dp[i-1][j]+inp[j-1], dp[i-1][j-1]+inp[j-1])


print(max(dp[n]))
