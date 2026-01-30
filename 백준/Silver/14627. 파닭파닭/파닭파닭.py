import sys
input = sys.stdin.readline

s, c = map(int, input().split())
arr = []

low = 1
high = -1
max_len = 1
sum_val = 0
for _ in range(s):
    inp = int(input().rstrip())
    arr.append(inp)
    sum_val += inp
    if(high < inp):
        high = inp

while low <= high:
    mid = (low+high)//2

    cnt = 0
    for a in arr:
        cnt += a//mid

    if(cnt >= c):
        max_len = mid
        low = mid + 1
    else:
        high = mid - 1


print(sum_val - (max_len * c))