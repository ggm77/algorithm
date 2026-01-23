import sys
input = sys.stdin.readline

# 입력 받은 좌표 하나 하나 읽어가며 x값과 같은게 몇번 나왔는지 * y값과 같은게 몇번 나왔는지

x_cnt = [0] * 100001
y_cnt = [0] * 100001

x = []
y = []

n = int(input().rstrip())

for _ in range(n):
    inp1, inp2 = map(int, input().split())

    x.append(inp1)
    y.append(inp2)

    x_cnt[inp1] += 1
    y_cnt[inp2] += 1

result = 0
for i in range(n):
    result += (x_cnt[x[i]]-1)*(y_cnt[y[i]]-1)

print(result)