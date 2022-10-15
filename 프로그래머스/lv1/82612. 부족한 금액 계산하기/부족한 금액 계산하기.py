def solution(price, money, count):
    #answer = -1
    all_p = 0
    for i in range(1,count+1):
        all_p += price*i
    if(money-all_p)>= 0:
        return 0
    else :
        return all_p - money