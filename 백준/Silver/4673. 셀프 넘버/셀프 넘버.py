def check(n):
    if(n > 10000):
        return
    temp = n + sum(list(map(int, str(n))))
    if(temp < 10000):
        num[temp-1] = 0
    return check(temp)

num = [x for x in range(1, 10001)]
num[-1] = 0

for n in num:
    if(n != 0):
        print(n)
        check(n)