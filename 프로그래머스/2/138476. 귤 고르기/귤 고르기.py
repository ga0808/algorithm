from collections import Counter
def solution(k, tangerine):
    answer = 0
    cnt_dict = Counter(tangerine)
    t_sorted = sorted(cnt_dict.items(), key= lambda items : items[1], reverse=True)
    sum_k = 0
    
    for idx, t in enumerate(t_sorted):
        sum_k += t[1]
        if sum_k >= k:
            answer = idx+1
            break
    return answer