import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()
arr = []
for _ in range(n):
    arr.append(int(input().rstrip()))

stack = deque()

for s in string:
    if(s.isalpha()):
        stack.append(arr[ord(s)-ord('A')])
    else:
        second = stack.pop()
        first = stack.pop()

        if(s == '+'):
            stack.append(first + second)
        elif(s == '-'):
            stack.append(first - second)
        elif(s == '*'):
            stack.append(first * second)
        elif(s == '/'):
            stack.append(first / second)

print(f"{stack.pop():.2f}")