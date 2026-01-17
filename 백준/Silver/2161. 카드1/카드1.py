n = int(input())

card = [x for x in range(1, n+1)]
used = []

reverse = 1
while(len(card) > 1):
    if(reverse > 0):
        used.append(card.pop(0))
    else:
        card.append(card.pop(0))
    reverse *= -1

used.append(card[-1])
print(*used)