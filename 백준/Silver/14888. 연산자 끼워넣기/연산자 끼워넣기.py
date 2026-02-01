import sys
input = sys.stdin.readline

def cal(here, val, op):

    global max_val
    global min_val

    if(here >= n):
        if(max_val < val):
            max_val = val
        if(val < min_val):
            min_val = val
        return

    num = arr[here]

    if(op[0] != 0):
        op[0] -= 1
        cal(here+1, val+num, op)
        op[0] += 1
    if(op[1] != 0):
        op[1] -= 1
        cal(here+1, val-num, op)
        op[1] += 1
    if(op[2] != 0):
        op[2] -= 1
        cal(here+1, val*num, op)
        op[2] += 1
    if(op[3] != 0):
        op[3] -= 1
        cal(here+1, int(val/num), op)
        op[3] += 1

n = int(input().rstrip())
arr = list(map(int, input().split()))
operator_inp = list(map(int, input().split()))

max_val = -2000000001
min_val = 2000000001

cal(1, arr[0], operator_inp)

print(max_val)
print(min_val)