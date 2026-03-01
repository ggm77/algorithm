import sys
input = sys.stdin.readline

"""


"""

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(k):
        temp = 0
        for l in range(m):
            temp += a[i][l]*b[l][j]
        print(temp, end=" ")
    print("")