import sys
input = sys.stdin.readline

def check(here, arr):
    if(len(arr) == int(n/2)):
        check_list.append(list(arr))
        return

    for i in range(here, n+1):
        arr.append(i)
        check(i+1, arr)
        arr.pop()

def get_score(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            result += inp[arr[i]-1][arr[j]-1] + inp[arr[j]-1][arr[i]-1]
    return result


n = int(input().rstrip())

inp = []
for _ in range(n):
    inp.append(list(map(int, input().split())))

check_list = []
check(1, [])

min_val = 10000000
for i in range(int(len(check_list)/2)):
    temp = abs(get_score(check_list[i])-get_score(check_list[-(i+1)]))
    if(temp < min_val):
        min_val = temp

print(min_val)
