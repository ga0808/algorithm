def solution(n):
    fin_num = n//2 
    cnt = 0
    for i in range(1,fin_num+1): 
        sum = i
        plus_num = i
        while True:
            if sum == n:
                cnt += 1
                break
            elif sum > n:
                break
            plus_num += 1
            sum += plus_num
    return cnt + 1
