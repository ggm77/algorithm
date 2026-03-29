import sys
input = sys.stdin.readline

"""


"""

s = int(input().rstrip())

arr = []
sumVal = 0

i = 1
while (s > sumVal):
    sumVal += i
    arr.append(i)
    i += 1

target = sumVal - s

while (target != 0):
    if (target-1 <= len(arr)-1 and 0 <= target-1):
        target -= arr.pop(target-1)
    else:
        target -= arr.pop(-1)

print(len(arr))