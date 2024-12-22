def solution(arr1, arr2):
    answer = [ [0]*len(arr2[0]) for i in range(len(arr1)) ]
    
    for row_idx , arr_one in enumerate(arr1): 
        for col_idx in range(len(arr2[0])): 
            num = 0 
            for idx, num_1 in enumerate(arr_one): 
                num += (num_1 * arr2[idx][col_idx])
            answer[row_idx][col_idx] = num


    # print(answer)
    return answer