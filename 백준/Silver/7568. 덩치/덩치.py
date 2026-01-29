import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))

for i in range(len(arr)):
    cnt = 1
    for j in range(len(arr)):
        if(i != j):
            if(arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]):
                cnt += 1
    print(cnt, end=" ")