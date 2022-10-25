def solution(s):
    answer = ''
    nums_lst = list(map(int,s.split(" ")))
    answer += str(min(nums_lst))+" "
    answer += str(max(nums_lst))
    
    return answer