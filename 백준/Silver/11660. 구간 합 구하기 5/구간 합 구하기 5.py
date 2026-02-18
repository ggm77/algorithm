import sys
input = sys.stdin.readline

"""

"""

n, m = map(int, input().split())

arr = []

for _ in range(n):
    inp = list(map(int, input().split()))
    temp = []
    sum_val = 0
    for i in inp:
        sum_val += i
        temp.append(sum_val)
    arr.append(temp)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    result = 0
    for i in range(x1-1, x2):
        if(y1-2 >= 0):
            result += arr[i][y2-1] - arr[i][y1-2]
        else:
            result += arr[i][y2-1]

    print(result)

