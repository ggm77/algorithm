import sys
input = sys.stdin.readline

inp = list(input().rstrip())

for i in range(len(inp)):
    if(inp[i] == '-'):
        inp[i] = '0'

score = 0
half_frame = 0
# half_frame=19 == 10프레임 첫번째
i = 0
while(i < len(inp)):
    half_frame += 1
    if(inp[i] == 'P'):
        cur = 10-int(inp[i-1])
    elif(inp[i] == 'S'):
        cur = 10
        if(half_frame <= 17):
            half_frame += 1
    else:
        cur = int(inp[i])

    bonus = 0
    if(i != 0 and half_frame <= 19 and (inp[i-1] == 'S' or inp[i-1] == 'P')):
        bonus += 1
    if(i > 1 and half_frame <= 20 and inp[i-2] == 'S'):
        bonus += 1

    score += cur + cur*bonus

    i += 1

print(score)