import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    team_list = [[0,0,0,0,0] for _ in range(201)]
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        team_list[arr[i]-1][0] += 1
        team_list[arr[i]-1][1] = arr[i]
    
    score = 1
    for i in range(len(arr)):
        if(team_list[arr[i]-1][0] >= 6):
            if(team_list[arr[i]-1][4] <= 3):
                team_list[arr[i]-1][2] += score
            if(team_list[arr[i]-1][4] <= 4):
                team_list[arr[i]-1][3] += score
            team_list[arr[i]-1][4] += 1
            score += 1

    team_list.sort(key=lambda x: x[3])
    team_list.sort(key=lambda x: x[2])

    for team in team_list:
        if(team[0] >= 6):
            print(team[1])
            break
    
