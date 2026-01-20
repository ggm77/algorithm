import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

if(sum(arr) == 0):
    print(0)
else:
    arr.sort()

    for k in range(n, -1, -1):
        if(k == 0):
            print(k)
            break
        
        if(arr[n-k] >= k):
            con1 = True
        else:
            con1 = False

        if(k == n):
            con2 = True
        elif(arr[n-k-1] <= k):
            con2 = True
        else:
            con2 = False

        if(con1 and con2):
            print(k)
            break
