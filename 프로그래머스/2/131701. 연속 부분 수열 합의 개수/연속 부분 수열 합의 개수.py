def solution(elements):
    sum_lst = set(elements) 
    max_idx = len(elements) 
    
    for length in range(2,len(elements)+1): #길이
        for start in range(len(elements)): #시작 인덱스
            if start+length > max_idx:
                sum_lst.add(sum(elements[start:]) + sum(elements[:length - (max_idx - start)]))
                continue
            sum_lst.add(sum(elements[start:start+length]))
    answer = len(sum_lst)
    # print(sum_lst)
    return answer