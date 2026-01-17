import sys

n = int(sys.stdin.readline().rstrip())

materials = list(sys.stdin.readline().split())
used_materials = list(sys.stdin.readline().split())

for m in materials:
    if(m not in used_materials):
        print(m)
        break