import sys


while True:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break

    raw_words = []
    lowercase_words = []

    for _ in range(n):
        s = sys.stdin.readline().rstrip()
        raw_words.append(s)
        lowercase_words.append(s.lower())

    lowercase_words.sort()

    for i in range(n):
        if(raw_words[i].lower() == lowercase_words[0]):
            print(raw_words[i])
            break