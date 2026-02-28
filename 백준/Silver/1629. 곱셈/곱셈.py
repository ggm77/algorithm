import sys
input = sys.stdin.readline

"""

(a**b)%c

"""

def power(a, b, c):
    if b == 1:
        return a%c
    
    temp = power(a, b//2, c)

    if b%2 == 0:
        return (temp**2)%c
    else:
        return (temp**2 * a)%c

a, b, c = map(int, input().split())

print(power(a,b,c))