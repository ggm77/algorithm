import sys
input = sys.stdin.readline

"""

"""

n, m, k = map(int, input().split())

inp_arr = []
arr = [([0]*(m+1)) for _ in range(n+1)]

for _ in range(n):
    inp_arr.append(list(input().rstrip()))

for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

        if((i+j)%2 == 0 and inp_arr[i-1][j-1] == 'W'):
            arr[i][j] += 1
        if((i+j)%2 == 1 and inp_arr[i-1][j-1] == 'B'):
            arr[i][j] += 1

min_val = 5000000
for i in range(k, n+1):
    for j in range(k, m+1):
        temp = arr[i][j] - arr[i-k][j] - arr[i][j-k] + arr[i-k][j-k]
        min_val = min(min_val, temp, k**2-temp)

print(min_val)

