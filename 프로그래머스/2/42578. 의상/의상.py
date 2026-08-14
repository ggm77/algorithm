def solution(clothes):
    answer = 1
    
    db = {}
    
    for c in clothes:
        if c[1] in db.keys():
            db[c[1]].append(c[0])
        else:
            db[c[1]] = [c[0]]
        
        
    for key in db.keys():
        answer *= len(db[key])+1
    
    return answer - 1