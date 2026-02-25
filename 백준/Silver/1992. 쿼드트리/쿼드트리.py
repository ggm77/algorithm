import sys
input = sys.stdin.readline

"""

"""

def check(x, y, n):
    temp = 0
    for i in range(y, y+n):
        temp += sum(arr[i][x:x+n])
    
    if (temp == n**2):
        return "1"
    elif (temp == 0):
        return "0"
    else:
        n = int(n/2)
        return f"({check(x,y,n)+check(x+n,y,n)+check(x,y+n,n)+check(x+n,y+n,n)})"

n = int(input().rstrip())

arr = []
for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))

print(check(0,0,n))