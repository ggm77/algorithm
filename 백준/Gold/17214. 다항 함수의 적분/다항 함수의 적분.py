import sys
input = sys.stdin.readline

def toStr(n):
    if(n == 0):
        return ""
    elif(n == 1):
        return "+x"
    elif(n == -1):
        return "-x"
    elif(n > 0):
        return "+"+str(n)+"x"
    else:
        return str(n)+"x"

string = input().rstrip()

if(string[0] != '-'):
    string = "+"+string

string += '@'

last_index = 0
x = -30000
n = -30000
for i in range(len(string)):
    if(i != 0 and not string[i].isdecimal()):
        temp = string[last_index:i]

        if(len(temp) > 0):
            if(temp == "+"):
                num = 1
            elif(temp == "-"):
                num = -1
            else:
                num = int(temp)

            if(string[i] == 'x'):
                last_index = i+1
                if(num != 0):
                    x = num
            else:
                last_index = i
                if(num != 0):
                    n = num

if(x == -30000 and n == -30000): # 아무값도 안들어옴
    print("W")
elif(x == -30000): # 상수항만 존재
    if(n == 1):
        print("x+W")
    elif(n == -1):
        print("-x+W")
    else:
        print(str(n) + "x+W")
elif(n == -30000): # 일차항만 존재
    if(x == 2):
        print("xx+W")
    elif(x == -2):
        print("-xx+W")
    else:
        print(str(int(x/2)) + "xx+W")
else: # 전부 존재
    if(x == 2):
        print("xx" + toStr(n)+"+W")
    elif(x == -2):
        print("-xx" + toStr(n)+"+W")
    else:
        print(str(int(x/2)) + "xx" + toStr(n)+"+W")