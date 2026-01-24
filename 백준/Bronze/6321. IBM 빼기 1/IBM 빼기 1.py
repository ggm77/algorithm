import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = []

for i in range(n):
    arr.append(input().rstrip())

for i in range(len(arr)):
    string = arr[i]
    print("String #"+str(i+1))
    for s in string:
        if(s == 'Z'):
            print('A', end="")
        else:
            print(chr(ord(s)+1), end="")
    print("\n")