def solution(k, score):
    ans = []
    res = []
    
    for i in score[:k]:
        ans.append(i)
        res.append(min(ans))
        
    for j in score[k:]:
        ans.append(j)
        ans.sort(reverse=True)
        del ans[-1]
        res.append(min(ans))
    return res