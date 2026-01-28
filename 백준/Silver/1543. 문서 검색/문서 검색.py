import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def search(s, q):
    if(len(s) < len(q)):
        return 0
    if(len(s) == len(q)):
        if(s == q):
            return 1
        else:
            return 0
    if(s[:len(q)] == q):
        return 1+search(s[len(q):], q)
    else:
        return search(s[1:], q)

string = input().rstrip()
query = input().rstrip()

print(search(string, query))

