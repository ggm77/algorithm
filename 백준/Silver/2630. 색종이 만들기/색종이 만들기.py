import sys
input = sys.stdin.readline

"""

"""

def check(x, y, n):
    temp = 0
    for i in range(y, y+n):
        temp += sum(arr[i][x:(x+n)])
    
    if(temp == 0):
        result[0] += 1
    elif(temp == n**2):
        result[1] += 1
    else:
        n = int(n/2)
        check(x, y, n)
        check(x+n, y, n)
        check(x, y+n, n)
        check(x+n, y+n, n)
    

n = int(input().rstrip())

result = [0,0]

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

check(0, 0, n)

print(result[0])
print(result[1])