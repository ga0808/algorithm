def solution(topping):
    part_1 = {}
    part_2 = {}
    
    for t in topping:
        if t not in part_2:
            part_2[t] =1
        else:
            part_2[t] +=1
    
    answer = 0
    for t in topping:
        if t not in part_1:
            part_1[t] = 1
        else : 
            part_1[t] += 1
            
        part_2[t] -= 1
        
        if part_2[t] == 0 :
            del part_2[t]
        if len(part_1) == len(part_2):
            answer += 1
        
    return answer