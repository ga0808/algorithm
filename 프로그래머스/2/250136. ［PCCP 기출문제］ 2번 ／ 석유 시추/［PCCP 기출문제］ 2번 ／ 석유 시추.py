from pprint import pprint
from copy import deepcopy
import sys
# print(sys.__dir__())
sys.setrecursionlimit(int(10**9))

def solution(land):
    #행, 열 인덱스
    def dfs(i,j,visited_land,return_lst):

        #탐색 불가 
        if i<0 or j<0 or i>=n or j>=m:
            return return_lst
        
        #탐색 안한 곳 (석유가 있는 곳으로 체킹안한 곳)
        if visited_land[i][j]==1:
            #석유 덩어리가 존재하는 가장 큰 컬럼 값
            if return_lst[1] < j:
                return_lst[1] = j
            visited_land[i][j] = 0
            return_lst[0] += 1
            dfs(i-1,j,visited_land,return_lst)
            dfs(i+1,j,visited_land,return_lst)
            dfs(i,j-1,visited_land,return_lst)
            dfs(i,j+1,visited_land,return_lst) 
            return return_lst
        return return_lst
    
    visited_land = deepcopy(land)
    n = len(land)
    m = len(land[0])
    
    #석유 양 계속 더하여 갱신할 리스트
    oil_lst = [0]*m

    for col in range(m):
        for row in range(n):
            return_lst = [0, col]
            if land[row][col] == 1 :
                oil_quantity, col_range = dfs(row,col,visited_land,return_lst)
                # print(col,col_range, oil_quantity)
                if oil_quantity!=0:
                    # print(oil_quantity,col,col_range )
                    # print("!=0",col,col_range, oil_quantity)
                    for c in range(col,col_range+1):
                        # print("c",c)
                        oil_lst[c] += oil_quantity
    # print(oil_lst)
    return max(oil_lst)