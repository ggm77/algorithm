n = int(input())

result = 0

for num in range(1, n+1):
    n = sum(map(int, str(num)))
    if(num%n == 0):
        result += 1

print(result)