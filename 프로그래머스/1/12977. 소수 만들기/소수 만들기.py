from itertools import combinations
def solution(nums):
    answer = 0
    comb_lst = list(combinations(nums, 3))
    
    for c in comb_lst:
        chk = 0
        n = sum(c)
        for i in range(2,n//2):
            if n % i == 0 :
                chk = 1
                break
        if chk == 0 :
            answer += 1

    return answer