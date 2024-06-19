def solution(n, computers):
    answer = 0
    visited = [0]*n
    
    #dfs : 연결된 컴퓨터들을 깊이 탐색 -> 연결된 하나의 네트워크를 탐색
    def dfs(row):
        if visited[row] == 1:
                return 0
        
        visited[row] += 1
        
        for idx, c in enumerate(computers[row]):

            if c == 0 or idx==row:
                continue
            dfs(idx)
            
    for row, visit in enumerate(visited):
        if visit == 1:
            continue
        answer += 1
        dfs(row)
    
    return answer