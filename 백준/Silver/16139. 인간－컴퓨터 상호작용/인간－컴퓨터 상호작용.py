import sys
input = sys.stdin.readline

string = input().rstrip()
q = int(input().rstrip())

arr = []
temp = [0] * 26

for s in string:
    temp[ord(s)-ord('a')] += 1
    arr.append(temp.copy())

for _ in range(q):
    a, l, r = input().split()
    result = arr[int(r)][ord(a)-ord('a')] - arr[int(l)][ord(a)-ord('a')]

    if(string[int(l)] == a):
        print(result+1)
    else:
        print(result)