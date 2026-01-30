n = int(input().rstrip())

base = "* " * n

for i in range(n):
    if(i%2 == 0):
        print(base)
    else:
        print("", base)