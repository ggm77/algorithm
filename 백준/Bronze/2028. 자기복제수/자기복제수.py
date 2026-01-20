import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    original_string = str(n)
    string = str(n**2)

    if(original_string == string[len(string)-len(original_string):]):
        print("YES")
    else:
        print("NO")