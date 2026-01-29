import sys
input = sys.stdin.readline

inp = input().rstrip()

no_zero = inp.replace("0", " ")
no_one = inp.replace("1", " ")

print(min(len(no_zero.split()), len(no_one.split())))