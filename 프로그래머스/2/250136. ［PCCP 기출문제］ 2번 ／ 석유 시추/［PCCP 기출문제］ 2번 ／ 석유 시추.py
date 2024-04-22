from copy import deepcopy
import sys
sys.setrecursionlimit(int(10**9))

def dfs(row,col,r,c,land,return_lst):
    #land 범위 밖
    if r<0 or c<0 or r>=row or c>=col:
        return return_lst
    
    #석유 존재하는 곳
    if land[r][c] == 1:
        #시추 처리
        land[r][c] = 0
        #시추된 석유양 +1
        return_lst[0] += 1
        
        if return_lst[1] < c:
            return_lst[1] = c
            
        dfs(row,col,r-1,c,land,return_lst)
        dfs(row,col,r+1,c,land,return_lst)
        dfs(row,col,r,c-1,land,return_lst)
        dfs(row,col,r,c+1,land,return_lst)
        return return_lst
    
    return return_lst

def solution(land):
    #행
    row = len(land)
    #열
    col = len(land[0])

    oil_lst = [0]*col
    
    for c in range(col):
        
        for r in range(row):
            return_lst = [0,c]
            if land[r][c] == 1:
                oil_quantity, col_range = dfs(row,col,r,c,land,return_lst)
                if oil_quantity != 0:
                    for o_c in range(c, col_range+1):
                        oil_lst[o_c] += oil_quantity
    return max(oil_lst)