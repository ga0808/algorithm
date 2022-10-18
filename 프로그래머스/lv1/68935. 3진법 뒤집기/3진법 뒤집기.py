def solution(n):
    ten_num = 0
    three_num = []
    x = 0 
    while n>0:
        one = n%3
        three_num.append(one)
        n = n//3

    for i in range(len(three_num)-1,-1,-1): #1 # 2 #0
        ten_num += ((3**x) * three_num[i])
        x+=1
    return ten_num 