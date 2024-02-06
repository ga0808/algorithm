def solution(numbers, target):
    # +, - 

    #+4+1+2+1
    #      -1
    #+4+1-2+1
    #+4+1  -1
    

    # [4,1,2,1]
    # -4+1+2+1
    #.  -1+2+1

    #방문처리 - 안해도 될것 같은데? - 그 뒤의 숫자들을 순차적으로 하면되니까
    cnt = 0 
    def dfs(numbers,n,target,num_sum): #n = 시작 인덱스
        
        if n == len(numbers):
            if num_sum == target:
                nonlocal cnt 
                cnt +=1
            num_sum = 0
            return
        
        #+로 넘어가기
        num_sum += numbers[n]
        dfs(numbers,n+1,target,num_sum) 
        #dfs(1) - 밑dfs(1) 킵 , num_sum=4
        #dfs(2) - 밑 dfs(2)킵 , num_sum=5
        #dfs(3) - 밑 dfs(3)킵 , num_sum=7
        #dfs(4) -- return , cnt =1, num_sum = 0
        #킵된거
        #밑 dfs(3) -> num_sum=7   - > 
        
        # - 로 넘어갈때
        num_sum -= (2*numbers[n])
        dfs(numbers,n+1,target,num_sum)

    dfs(numbers,0,target,0)
    return cnt