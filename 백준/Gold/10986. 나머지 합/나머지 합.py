import sys
input = sys.stdin.readline

"""

"""

n, m = map(int, input().split())

inp = list(map(int, input().split()))
arr = [0] * (m+1)
result = 0
sum_val = 0
for i in inp:
    sum_val += i
    temp = sum_val%m
    if(temp == 0):
        result += 1
    arr[temp] += 1


for a in arr:
    if(a > 1):
        result += a*(a-1)/2

print(int(result))

