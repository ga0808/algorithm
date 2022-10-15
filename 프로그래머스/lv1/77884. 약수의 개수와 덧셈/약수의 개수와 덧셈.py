def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        cnt_lst = []
        for j in range(1,i+1):
            if i%j ==0:
                cnt_lst.append(j)
               # print(cnt_lst)
        if len(cnt_lst)%2 ==0:
            answer += i
        elif len(cnt_lst)%2 !=0:
            answer -= i    
    return answer