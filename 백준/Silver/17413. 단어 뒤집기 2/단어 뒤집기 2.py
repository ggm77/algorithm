import sys
input = sys.stdin.readline

string = input().rstrip()

i = 0
while i < len(string):
    if(string[i] == '<'):
        string = string[:i] + '@' + string[i:]
        i += 1
    elif(string[i] == '>'):
        string = string[:i+1] + '@' + string[i+1:]
        i += 1
    i += 1

string_list = list(string.split("@"))
# print(string_list)

for s in string_list:
    if(len(s) != 0):
        if(s[0] == "<"):
            print(s, end="")
        else:
            if(s[0] == " "):
                print(" ", end="")
            temp = s.split()
            for i in range(len(temp)):
                if(i != len(temp)-1):
                    print(temp[i][::-1], end=" ")
                else:
                    print(temp[i][::-1], end="")
            if(len(s) != 1 and s[-1] == " "):
                print(" ", end="")