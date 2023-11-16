def solution(n):
    if n <= 3:
        return 0
    
    cnt = 0
    for i in range(4,n+1):
        div = i//2
        for d in range(2,div+1):
            if i%d == 0:
                cnt +=1
                break

    return cnt