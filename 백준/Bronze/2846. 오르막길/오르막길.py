import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))

max_val = 0
start_val = -1
is_asc = False
for i in range(len(arr)):
    if(not is_asc and i != 0 and arr[i-1] < arr[i]):
        is_asc = True
        start_val = arr[i-1]
    if((i != len(arr)-1 and arr[i+1] <= arr[i] and is_asc) or (i == len(arr)-1 and is_asc)):
        if(max_val < arr[i]-start_val):
            max_val = arr[i]-start_val
        is_asc = False

print(max_val)