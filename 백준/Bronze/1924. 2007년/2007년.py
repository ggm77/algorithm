def md_to_day(m, d):
    for i in range(1, m):
        d += month[i]

    return d

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
type = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

m, d = map(int, input().split())

print(type[md_to_day(m, d)%7])