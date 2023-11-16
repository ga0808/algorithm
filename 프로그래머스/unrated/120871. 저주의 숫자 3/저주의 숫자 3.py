def solution(n):
    if n <= 2:
        return n
    
    t_num = 3
    for i in range(3,n+1):
        t_num+=1
        
        #3으로 나누어떨어지거나, 3이 포함되지 않을때까지 반복
        if t_num % 3 ==0 or "3" in str(t_num):
            while True:
                if t_num % 3 ==0 or "3" in str(t_num):
                    t_num += 1
                else:
                    break
            
    return t_num