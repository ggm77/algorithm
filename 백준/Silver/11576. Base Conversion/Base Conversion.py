import sys
input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input().rstrip())
arr = list(map(int, input().split()))
arr = arr[::-1]

ten = arr[0]
for i in range(1, len(arr)):
    ten += arr[i] * (a**i)

result = []
while ten != 0:
    result.append(ten%b)
    ten = ten//b

print(*(result[::-1]))