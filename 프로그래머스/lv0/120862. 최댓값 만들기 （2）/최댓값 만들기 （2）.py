def solution(numbers):
    
    num_lst = []
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            num_lst.append(numbers[i] * numbers[j])
    answer = max(num_lst)
    return answer