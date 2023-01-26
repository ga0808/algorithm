def solution(clothes):
    from itertools import combinations, permutations, product
    answer = 0
    res = 1
    c_dict = {}
    for c in clothes:
        if c[1] not in c_dict.keys():
            c_dict[c[1]] = 1
        elif c[1] in c_dict.keys():
            c_dict[c[1]] += 1
    for i in c_dict.values():
        res *= (i+1)
    # for i in range(1,len(c_dict.values())+1):
    #     for j in combinations(c_dict.values(),i):
    #         print(j)
    
    return res-1