import sys
input = sys.stdin.readline

# nHm-n n개 중에서 중복 혀용해서 m-n개 뽑기
# n+m-n-1Cm-n = m-1Cm-n

n = int(input().rstrip())
m = int(input().rstrip())

result = 1

for i in range(m-1, m-1-(m-n), -1):
    result *= i
for i in range(2, m-n+1):
    result /= i

print(int(result))