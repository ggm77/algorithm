def solution(answers):
    
    answer = []
    
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    s1_index = 0
    s2_index = 0
    s3_index = 0
    
    s1_score = 0
    s2_score = 0
    s3_score = 0
    max_score = -1
    
    for a in answers:
        if(a == s1[s1_index]):
            s1_score += 1
        if(s1_index == len(s1)-1):
            s1_index = 0
        else:
            s1_index += 1
        if(a == s2[s2_index]):
            s2_score += 1
        if(s2_index == len(s2)-1):
            s2_index = 0
        else:
            s2_index += 1
        if(a == s3[s3_index]):
            s3_score += 1
        if(s3_index == len(s3)-1):
            s3_index = 0
        else:
            s3_index += 1
        if(max_score < s1_score):
            max_score = s1_score
        if(max_score < s2_score):
            max_score = s2_score
        if(max_score < s3_score):
            max_score = s3_score
    
    if(s1_score == max_score):
        answer.append(1)
    if(s2_score == max_score):
        answer.append(2)
    if(s3_score == max_score):
        answer.append(3)
    
    return answer