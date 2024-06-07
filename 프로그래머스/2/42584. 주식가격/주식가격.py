from collections import defaultdict

def solution(prices):
    idx_dict = defaultdict(list)
    answer = [0] * len(prices)
    
    for idx, tmp in enumerate(prices):
        for cmp, indices in list(idx_dict.items()):
            if tmp < cmp: #현재 p보다 큰 p 존재
                for i in indices:
                    answer[i] = idx - i
                del idx_dict[cmp]
            
        idx_dict[tmp].append(idx)
    
    for indices in idx_dict.values():
        for i in indices:
            answer[i] = idx - i
    return answer