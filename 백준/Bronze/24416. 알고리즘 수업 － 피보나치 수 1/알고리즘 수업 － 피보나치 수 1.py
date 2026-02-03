import sys
input = sys.stdin.readline

def fib1(n):
    global cnt1

    if(n < 3):
        cnt1 += 1
        return 1
    return fib1(n-1) + fib1(n-2)

def fib2(n):
    global cnt2
    
    dp = [1, 1]
    for i in range(3, n+1):
        cnt2 += 1
        dp.append(dp[i-2] + dp[i-3])
    return dp[-1]

    


n = int(input().rstrip())

cnt1 = 0
cnt2 = 0

fib1(n)
fib2(n)

print(cnt1, cnt2)