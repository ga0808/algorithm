def solution(a, b):
    sum_lst = []
    for i in range(0,len(a)):
        sum_lst.append(a[i] * b[i])
    answer = sum(sum_lst)
    return answer