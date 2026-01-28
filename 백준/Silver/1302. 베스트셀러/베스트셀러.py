import sys
input = sys.stdin.readline

n = int(input().rstrip())

book = {}

for _ in range(n):
    inp = input().rstrip()
    if(inp in book.keys()):
        book[inp] += 1
    else:
        book[inp] = 1

book_list = sorted(book.items())
book_list.sort(key=lambda x: x[1], reverse=True)

print(book_list[0][0])
