def solution(q1, q2):
    
    q = q1+q2+q1
    
    q1_start = 0
    q2_start = len(q2)
    
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    
    ans = 0
    while True:
        if q1_start == q2_start:
            return -1
        elif q2_start == len(q)-1:
            return -1
        
        # if q1_start!=0 and q1 == q[q1_start:]:
        #     return -1
        
        if q1_sum == q2_sum:
            return ans   
        elif q1_sum > q2_sum:
            tmp = q[q1_start]
            q1_sum -= tmp
            q2_sum += tmp
            q1_start +=1
            ans+=1
            
        else :
            tmp = q[q2_start]
            q1_sum += tmp
            q2_sum -= tmp
            q2_start +=1
            ans+=1
            
        # print(q)
        # print(q1_start)
        # print(q1_sum)
        # print(q2_start)
        # print(q2_sum)
        # print("==========")
    
    return answer