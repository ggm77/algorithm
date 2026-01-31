import sys
input = sys.stdin.readline

"""
t = n - m
nCm = n! / (m! * t!)

"""

n, m = map(int, input().split())
t = n-m


cnt_2 = 0
cnt_5 = 0

for i in range(1, 40):
    two = 2**i
    five = 5**i
    if(two <= n):
        cnt_2 += n//two
    if(five <= n):
        cnt_5 += n//five
    if(two <= m):
        cnt_2 -= m//two
    if(five <= m):
        cnt_5 -= m//five
    if(two <= t):
        cnt_2 -= t//two
    if(five <= t):
        cnt_5 -= t//five
    if(two > n and two > m and two > t):
        break

print(min(cnt_2, cnt_5))
