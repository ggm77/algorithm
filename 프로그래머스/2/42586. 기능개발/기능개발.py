def solution(progresses, speeds):
    answer = []
    
    while len(progresses) != 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        deployCount = 0
        while len(progresses) != 0:
            if (progresses[0] >= 100):
                progresses.pop(0)
                speeds.pop(0)
                deployCount += 1
            else:
                break
                
        if (deployCount != 0):
            answer.append(deployCount)
    
    return answer