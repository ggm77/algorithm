import sys
input = sys.stdin.readline

x, y = map(int, input().split())
n = int(input().rstrip())

# 1000그람당 가격 최솟값
min_cost = x/y*1000

for _ in range(n):
    x, y = map(int, input().split())
    temp = x/y*1000
    if(temp < min_cost):
        min_cost = temp

print(f"{min_cost:.2f}")