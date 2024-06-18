def solution(n, computers):
    answer = 0
    visited = [0]*n
    
    def dfs(row):
        # nonlocal answer
        visited[row] +=1
        # print("visited",visited)
        # print("row", row,"="*10)
        #row : 0 > 1
        
#         if sum(computers[row]) == 1:
#             answer += 1
#             return 0

#         if row == n-1 : 
#             answer += 1 
#             return 0
        
        
        # print("computers[row]",computers[row])
        for idx, c in enumerate(computers[row]):
            
            if visited[idx] == 1 or idx == row:
                # print("pass",idx, c)
                continue
            
            # print("search",idx, c)
            
            if c == 1:
                dfs(idx)  
    
    for row, visit in enumerate(visited):
        if visit == 0:
            answer += 1
            dfs(row)
    
    return answer