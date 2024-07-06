def solution(k, dungeons):
#모든 순열
    max_explo_cnt = 0
    
    def dfs(before_idx,k,explo_cnt,visited):
        nonlocal max_explo_cnt
        
        if explo_cnt > max_explo_cnt:
            max_explo_cnt = explo_cnt
            
        if k==0:
            return 0
        
        for idx, val in enumerate(dungeons):
            if (idx == before_idx )or (k < val[0]) or (visited[idx]==1) : #지금 탐험한 것
                continue
            #탐험 가능한 것만 
            copy_visited = visited[:]
            copy_visited[idx] = 1
            dfs(idx,k-val[1],explo_cnt+1,copy_visited)
            
                
    #처음부터 k보다 커서 탐험할 수 없는 던전 제거
    for idx, d in enumerate(dungeons):
        if d[0] > k:
            dungeons.pop(idx)
    
    visited = [0]*len(dungeons)
    dfs(-1,k,0,visited)
    
    return max_explo_cnt