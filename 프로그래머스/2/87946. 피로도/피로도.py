def solution(k, dungeons):
    max_cnt = 0
    
    def dfs(idx,k,cnt,visited):
        nonlocal max_cnt
        
        if max_cnt < cnt:
            max_cnt = cnt
        
        if k == 0:
            return 0
        
        for i, d in enumerate(dungeons):
            if (d[0] > k) or (visited[i]==1):
                continue
            
            copy_visited = visited[:]
            copy_visited[i] = 1
            # print(d,cnt,copy_visited)
            dfs(i,k-d[1],cnt+1,copy_visited)
        
    for idx,d in enumerate(dungeons):
        if d[0] > k:
            dungeons.pop(idx)
    
    visited = [0]*len(dungeons)
    dfs(0,k,0,visited)
    
    return max_cnt