import sys
input = sys.stdin.readline

arr = []

for _ in range(9):
    arr.append(int(input().rstrip()))

for i in range(9):
    for j in range(9):
        if(i != j):
            temp1 = arr[i]
            temp2 = arr[j]
            arr[i] = 0
            arr[j] = 0
            if(sum(arr) == 100):
                for k in range(9):
                    if(arr[k] != 0):
                        print(arr[k])
                sys.exit(0)
            arr[i] = temp1
            arr[j] = temp2