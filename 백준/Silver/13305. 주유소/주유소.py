import sys
input = sys.stdin.readline

# 1번 도시보다 싼 도시가 나올 때 까지 거리 계산
# 그 도시 갈 만큼 주유
# 반복

n = int(input().rstrip())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

result = 0
curr = 0
while curr < len(cost)-1:
    next = len(cost)-1
    for i in range(curr+1, len(cost)):
        if(cost[curr] > cost[i]):
            next = i
            break
    
    result += cost[curr] * sum(distance[curr:next])
    curr = next

print(result)