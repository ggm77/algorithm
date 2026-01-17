import sys

n_a, n_b = map(int, sys.stdin.readline().split())

a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

result = sorted(a.difference(b))

print(len(result))
if(len(result) != 0):
    print(*result)