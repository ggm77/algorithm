import sys
input = sys.stdin.readline

"""


"""

n = int(input().rstrip())

if (n == 1 or n == 3):
    print("-1")
else:

    result = n//5
    n %= 5

    if (n%2 != 0):
        result -= 1
        n += 5

    result += n//2
    n %= 2

    print(result)
