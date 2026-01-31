import sys
input = sys.stdin.readline

"""
Ai - s들의 최대공약수
"""

def gcd(a, b):
    if(b == 0):
        return a
    
    return gcd(b, a%b)

def fuc(n):
    new = int(n)
    return abs(new-s)

n, s = map(int, input().split())

arr = list(map(fuc, input().split()))

if(len(arr) == 1):
    print(arr[0])
else:
    prev = arr[0]
    for i in range(1, len(arr)):
        prev = gcd(prev, arr[i])
    print(prev)

