def solution(dirs):
    
    curX = 0
    curY = 0
    
    visited = set()
    
    for s in dirs:
        if (s == 'U'):
            if (curY != 5):
                visited.add((curX,curY,curX,curY+1))
                curY += 1
        elif(s == 'D'):
            if (curY != -5):
                visited.add((curX,curY-1,curX,curY))
                curY -= 1
        elif(s == 'R'):
            if (curX != 5):
                visited.add((curX,curY,curX+1,curY))
                curX += 1
        elif(s == 'L'):
            if (curX != -5):
                visited.add((curX-1,curY,curX,curY))
                curX -= 1
    
    return len(visited)