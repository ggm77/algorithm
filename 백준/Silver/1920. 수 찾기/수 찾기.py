import sys
input = sys.stdin.readline

n = int(input().rstrip())
inp = list(map(int, input().split()))

a = {}
for i in inp:
    a[i] = 1;


m = int(input().rstrip())
test_case = list(map(int, input().split()))

for t in test_case:
    try:
        a[t]
        print("1")
    except KeyError:
        print("0")