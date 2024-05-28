def solution(priorities, location):
    answer = 0
    tmp_idx = location
    cnt = 0
    
    while True:
        #최댓값 찾고 -> 최댓값
        tmp_max = max(priorities) 
        max_idx = priorities.index(tmp_max) 
        
        priorities = priorities[max_idx+1:] + priorities[:max_idx]
        

        cnt +=1 
        
        #지금 제거한 tmp_max가 우리가 찾던값인지 확인
         #지금 제거한 값의 인덱스가 0이면 - 맞음
        if tmp_idx - max_idx ==0: 
            return cnt
        elif tmp_idx - max_idx<0:
            tmp_idx = len(priorities)-max_idx+tmp_idx
        else : 
            tmp_idx = tmp_idx - (max_idx+1) 
