from math import ceil

def solution(n):
    res = []
    end_num = 0
    for i in range(n):
        res.append([i+1]*(i+1))
        end_num += i+1
        if i+1 == n:
            res[-1][1:] = [j for j in range(i+2,2*n)] 
    #가능한 인덱스 
    end = 1
    start = n-2 
    
    e = (2*n)
    o = 1
    
    idx = start
    tmp = n-2
    #쭉
    j = n-2
    
        
    while e <= end_num:
        # print(tmp)
        # print(idx, end ,"====")
        res[idx][tmp] = e
        
        if idx == end: #올라가거나, 내려가는게 끝났을 때 (마지막 값까지 대입 완료)
            if o==1:
                end = start
                start = idx+1
            else:
                end = start + 1
                start = idx -1 
            o *= -1
                
            if o == 1: #내려가다가 -> 올라갈때
                while True:
                    e+=1
                    tmp+=1
                    if res[idx][tmp] == res[idx][0]:
                        res[idx][tmp] = e
                    else:
                        tmp-=1
                        e-=1
                        break
        if o == 1 :
            tmp -= 1 #3
            
        idx -= o
        e +=1
    
    answer = []
    for lst in res:
        answer.extend(lst)
    return answer

