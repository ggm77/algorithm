import sys
input = sys.stdin.readline

song = ["baby", "sukhwan", "tu", "tu", "very", "cute", "tu", "tu", "in", "bed", "tu", "tu", "baby", "sukhwan"]

n = int(input().rstrip())

cnt = n//14
word = n%14

if(song[word-1] != "tu"):
    print(song[word-1])
else:
    if(word%2 == 0):
        tu = 1+cnt
    else:
        tu = 2+cnt
    if(tu >= 5):
        print("tu+ru*"+str(tu))
    else:
        print("tu", end="")
        for i in range(tu):
            print("ru",end="")

