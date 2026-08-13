def solution(left, right):  
    import math
    
    answer = 0
    
    for i in range(left, right+1):
        if (i == math.isqrt(i)**2):
            answer -= i
        else:
            answer += i
    
    return answer