def solution(priorities, location):
    answer = 0
    
    while len(priorities) != 0:
        maxVal = max(priorities)
        
        while priorities[0] != maxVal:
            priorities.append(priorities.pop(0))
            
            if (location == 0):
                location = len(priorities)-1
            else:
                location -= 1
        
        priorities.pop(0)
        answer += 1
        
        if (location == 0):
            return answer
        else:
            location -= 1
        
    return answer