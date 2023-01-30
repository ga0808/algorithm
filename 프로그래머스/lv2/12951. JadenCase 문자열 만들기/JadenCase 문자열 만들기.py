def solution(s):
    answer = ''
    s_lst = s.split(" ")
    res_lst=[ i.capitalize() for i in s_lst]
    
    for r in res_lst:
        if res_lst[-1] == r:
            answer += str(r)
        else:
            answer += str(r)+" "        
    return answer