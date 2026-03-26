import sys
input = sys.stdin.readline

"""


"""

t = int(input().rstrip())

for _ in range(t):
    leftStack = []
    rightStack = []

    inp = list(input().rstrip())

    for i in inp:
        if (i == '<'):
            if (len(leftStack) != 0):
                rightStack.append(leftStack.pop())
        elif (i == '>'):
            if (len(rightStack) != 0):
                leftStack.append(rightStack.pop())
        elif (i == '-'):
            if (len(leftStack) != 0):
                leftStack.pop()
        else:
            leftStack.append(i)
    
    rightStack.reverse()

    print("".join(leftStack+rightStack))
