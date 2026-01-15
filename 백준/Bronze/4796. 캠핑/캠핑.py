import sys

cnt = 1
while(True):
    l, p, v = map(int, sys.stdin.readline().split())
    if(l == 0 and p == 0 and v == 0):
        break

    result = (v//p)*l

    if(v%p <= l):
        result += v%p
    else:
        result += l
    print("Case " + str(cnt) + ": " + str(result))
    cnt += 1