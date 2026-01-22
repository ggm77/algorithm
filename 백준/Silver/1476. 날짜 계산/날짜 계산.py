import sys
input = sys.stdin.readline

target_e, target_s, target_m = map(int, input().split())

result = 1
e = 1
s = 1
m = 1

while(e != target_e or s != target_s or m != target_m):
    e += 1
    s += 1
    m += 1
    result += 1

    if(e > 15):
        e = 1
    if(s > 28):
        s = 1
    if(m > 19):
        m = 1

print(result)