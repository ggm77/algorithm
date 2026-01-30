import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = list(map(int, input().split()))
arr.sort()

result = 0
for i in range(len(arr)):
    result += sum(arr[:i+1])

print(result)