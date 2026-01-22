import sys
input = sys.stdin.readline

m, n = map(int, input().split())

result = [0, 0, 0, 0, 0]

for i in range(m):
    temp = [0] * 101
    for j in range(5):
        string = input().rstrip()
        if(j != 0):
            for k in range(n):
                if(string[1+k*5] == '*'):
                    temp[k] += 1
    for j in range(n):
        result[temp[j]] += 1

print(*result)
    