import sys

def md_to_day(m, d):
    for i in range(1, m):
        d += month[i]

    if(d-59 < 1):
        return 1
    elif(d-59 > 276):
        return 276
    else:
        return d-59

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

n = int(sys.stdin.readline().rstrip())

flower = []

for _ in range(n):
    m1, d1, m2, d2 = map(int, sys.stdin.readline().split())
    flower.append([md_to_day(m1, d1), md_to_day(m2, d2)])

flower.sort(key=lambda x: x[0])

if(flower[0][0] != 1):
    print("0")
else:
    index = -1
    target_val = 1
    max_val = 1
    result = 0
    while(True):

        i = index+1
        pre = index
        while(i < len(flower) and flower[i][0] <= target_val):
            if(max_val < flower[i][1]):
                max_val = flower[i][1]
                index = i
            i += 1
        
        if(pre == index):
            print("0")
            break
        
        result += 1
        target_val = flower[index][1]
        if(flower[index][1] >= 276):
            print(result)
            break
        if(i >= len(flower)):
            print("0")
            break
    
