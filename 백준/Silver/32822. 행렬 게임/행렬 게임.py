import sys
input = sys.stdin.readline


n, m = map(int, input().split())

arr = []

alpha = [0] * n

for _ in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        arr[i][j] = abs(arr[i][j] - temp[j])
        if(i == 0):
            alpha[j] = arr[i][j]
        else:
            if(alpha[j] < arr[i][j]):
                alpha[j] = arr[i][j]

beta = list(map(int, input().split()))
result = 0

for be in beta:
    result += alpha[be-1]

print(result)