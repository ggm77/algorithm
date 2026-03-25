import sys
input = sys.stdin.readline

"""


"""

def preorder(here):

    print(chr(here+65), end="")

    if (tree[here][0] != -1):
        preorder(tree[here][0])
    if (tree[here][1] != -1):
        preorder(tree[here][1])

def inorder(here):

    if (tree[here][0] != -1):
        inorder(tree[here][0])

    print(chr(here+65), end="")
    
    if (tree[here][1] != -1):
        inorder(tree[here][1])

def postorder(here):

    if (tree[here][0] != -1):
        postorder(tree[here][0])

    if (tree[here][1] != -1):
        postorder(tree[here][1])

    print(chr(here+65), end="")

n = int(input().rstrip())

tree = [0] * 26

for _ in range(n):
    rootStr, leftStr, rightStr = map(str, list(input().rstrip().split(" ")))

    if (leftStr == '.'):
        left = -1
    else:
        left = ord(leftStr) - 65
    
    if (rightStr == '.'):
        right = -1
    else:
        right = ord(rightStr) - 65
    
    tree[ord(rootStr)-65] = [left, right]

preorder(0)
print()
inorder(0)
print()
postorder(0)
