import sys
input = sys.stdin.readline

n = input().rstrip()

print(format(int(n, 8), 'b'))