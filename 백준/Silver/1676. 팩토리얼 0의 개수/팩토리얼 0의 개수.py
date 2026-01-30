import sys
input = sys.stdin.readline

n = int(input().rstrip())

result = 0
for i in range(1, 20):
    if 5**i <= n:
        result += n//(5**i)

print(result)
