import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
if(m == 0):
    broken_buttons = []
else:
    broken_buttons = list(input().split())

buttons = list(set({"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}).difference(broken_buttons))
buttons.append(" ")

n_str = str(n)

close_val = -1
distance = 9999999
for b1 in buttons:
    for b2 in buttons:
        for b3 in buttons:
            for b4 in buttons:
                for b5 in buttons:
                    for b6 in buttons:
                        temp = b1+b2+b3+b4+b5+b6
                        if(temp == "      "):
                            number = 100
                        else:
                            number = int(temp.replace(" ", "", -1))

                        if(abs(n - number) < distance):
                            distance = abs(n-number)
                            close_val = number
                        if(abs(n - number) == distance and len(str(number)) < len(str(close_val))):
                            distance = abs(n-number)
                            close_val = number


use_button = len(str(close_val)) + abs(n - close_val)
if(use_button < abs(n - 100)):
    print(use_button)
else:
    print(abs(n - 100))