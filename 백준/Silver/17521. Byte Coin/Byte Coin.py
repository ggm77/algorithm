import sys
input = sys.stdin.readline

n, w = map(int, input().split())

s = []

for _ in range(n):
    s.append(int(input().rstrip()))

min_val = 51
max_val = -1
last_index = -1
i = 0
while i < n:
    if(i != n-1 and s[i+1] < s[i]):
        max_val = s[i]

        min_val = 51
        for j in range(i, last_index, -1):
            if(s[j] < min_val):
                min_val = s[j]
        w = w//min_val * max_val + w%min_val
        last_index = i
    elif(i == n-1):
        max_val = -1
        for j in range(last_index+1, n):
            if(max_val < s[j]):
                max_val = s[j]
                temp = j
        min_val = 51
        for j in range(last_index+1, temp):
            if(s[j] < min_val):
                min_val = s[j]
        if(max_val != -1 and min_val != 51):
            w = w//min_val * max_val + w%min_val
    i += 1

print(w)