import sys
import math
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if(x1 == x2 and y1 == y2 and r1 == r2):
        print("-1")
    elif(x1 == x2 and y1 == y2):
        print("0")
    elif((r1+r2) == distance or abs(r1-r2) == distance):
        print("1")
    elif(abs(r1-r2) < distance and (r1+r2) > distance):
        print("2")
    else:
        print("0")