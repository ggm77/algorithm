import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))

sum_val = sum(arr[:k])
max_val = sum_val
for i in range(n-k):
    sum_val -= arr[i]
    sum_val += arr[i+k]

    if(max_val < sum_val):
        max_val = sum_val

print(max_val)