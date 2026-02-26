import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""

"""

def check(x, y, n):
    allSame = True
    temp = arr[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if (temp != arr[i][j]):
                allSame = False
    
    if (allSame):
        if (temp == -1):
            result[0] += 1
            return
        elif (temp == 0):
            result[1] += 1
            return
        elif (temp == 1):
            result[2] += 1
            return
    
    n = int(n/3)
    check(x,y,n)
    check(x+n,y,n)
    check(x,y+n,n)
    check(x+n,y+n,n)
    check(x+n*2,y,n)
    check(x+n*2,y+n,n)
    check(x+n*2,y+n*2,n)
    check(x,y+n*2,n)
    check(x+n,y+n*2,n)

n = int(input().rstrip())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = [0,0,0]
check(0,0,n)

print(result[0])
print(result[1])
print(result[2])