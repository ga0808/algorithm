def solution(s):
    
    s_lst_lower = [s[i] for i in range(0,len(s)) if s[i].islower() == True]
    s_lst_lower.sort(reverse=True)
    s_lst_upper = [s[i] for i in range(0,len(s)) if s[i].isupper() == True]
    s_lst_upper.sort(reverse=True)
    s_lst = s_lst_lower + s_lst_upper
    answer = "".join(s_lst)
    return answer